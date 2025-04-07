from env import GridEnvironment
import numpy as np
import pygame
import random
import time
import csv
import os

EPISODES = 300
LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPSILON = 1.0
EPSILON_DECAY = 0.995
MIN_EPSILON = 0.05

ACTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

env = GridEnvironment()
q_table = np.zeros((10, 10, 4))

def get_state(pos):
    return tuple(pos)

def choose_action(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, 3)
    return np.argmax(q_table[state[0], state[1]])

def move(pos, action, static_obs, dynamic_obs):
    new_x = pos[0] + ACTIONS[action][0]
    new_y = pos[1] + ACTIONS[action][1]
    new_pos = [new_x, new_y]

    if 0 <= new_x < 10 and 0 <= new_y < 10 and new_pos not in static_obs and new_pos not in dynamic_obs:
        return new_pos
    return pos

# CSV Log Setup
log_file = 'performance_log.csv'
write_header = not os.path.exists(log_file)
with open(log_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    if write_header:
        writer.writerow(['Episode', 'Reward', 'Time(s)', 'Steps', 'Collisions', 'Epsilon'])

# Training Loop
for episode in range(EPISODES):
    env.agent_pos = [0, 0]
    state = get_state(env.agent_pos)
    done = False
    total_reward = 0
    collisions = 0
    steps_taken = 0

    start_time = time.time()

    for step in range(200):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        action = choose_action(state, EPSILON)
        new_pos = move(env.agent_pos, action, env.obstacles, env.dynamic_obstacles)
        new_state = get_state(new_pos)

        if new_pos == env.goal_pos:
            reward = 100
            done = True
        elif new_pos == env.agent_pos:
            reward = -10
            collisions += 1
        else:
            reward = -1
            steps_taken += 1

        old_value = q_table[state[0], state[1], action]
        next_max = np.max(q_table[new_state[0], new_state[1]])
        new_value = old_value + LEARNING_RATE * (reward + DISCOUNT * next_max - old_value)
        q_table[state[0], state[1], action] = new_value

        env.agent_pos = new_pos
        state = new_state
        total_reward += reward

        env.render()

        if done:
            break

    EPSILON = max(MIN_EPSILON, EPSILON * EPSILON_DECAY)
    elapsed_time = time.time() - start_time

    print(f"Episode {episode+1:3d} | Reward: {total_reward:4d} | Time: {elapsed_time:.2f}s | Steps: {steps_taken:3d} | Collisions: {collisions:2d} | Epsilon: {EPSILON:.3f}")

    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([episode+1, total_reward, round(elapsed_time, 2), steps_taken, collisions, round(EPSILON, 3)])

pygame.quit()