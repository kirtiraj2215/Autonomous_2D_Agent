import matplotlib.pyplot as plt
import csv

episodes = []
rewards = []
times = []
steps = []
collisions = []
epsilon_values = []

with open('performance_log.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        episodes.append(int(row[0]))
        rewards.append(int(row[1]))
        times.append(float(row[2]))
        steps.append(int(row[3]))
        collisions.append(int(row[4]))
        epsilon_values.append(float(row[5]))

# Plotting the data

fig, axs = plt.subplots(5, 1, figsize=(10, 15), sharex=True)

axs[0].plot(episodes, rewards, color='blue', label='Reward')
axs[0].set_ylabel('Reward')
axs[0].set_title('Reward vs Episodes')
axs[0].grid(True)

axs[1].plot(episodes, times, color='green', label='Time (seconds)')
axs[1].set_ylabel('Time (seconds)')
axs[1].set_title('Time vs Episodes')
axs[1].grid(True)

axs[2].plot(episodes, steps, color='red', label='Steps')
axs[2].set_ylabel('Steps')
axs[2].set_title('Steps vs Episodes')
axs[2].grid(True)

axs[3].plot(episodes, collisions, color='orange', label='Collisions')
axs[3].set_ylabel('Collisions')
axs[3].set_title('Collisions vs Episodes')
axs[3].grid(True)

axs[4].plot(episodes, epsilon_values, color='purple', label='Epsilon')
axs[4].set_xlabel('Episodes')
axs[4].set_ylabel('Epsilon')
axs[4].set_title('Epsilon vs Episodes')
axs[4].grid(True)

plt.tight_layout()
plt.show()