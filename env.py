import pygame
import random

CELL_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 10
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AGENT_COLOR = (0, 0, 255)
GOAL_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (100, 100, 100)
GRID_LINE_COLOR = (200, 200, 200)

class GridEnvironment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vyorius RL Agent with Dynamic Obstacles")
        self.clock = pygame.time.Clock()

        self.agent_pos = [0, 0]
        self.goal_pos = [GRID_WIDTH - 1, GRID_HEIGHT - 1]
        self.obstacles = self.generate_obstacles(10)
        self.dynamic_obstacles = self.generate_obstacles(5)

    def generate_obstacles(self, count):
        obs = []
        while len(obs) < count:
            pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
            if pos != self.agent_pos and pos != self.goal_pos and pos not in obs:
                obs.append(pos)
        return obs

    def update_dynamic_obstacles(self):
        for i in range(len(self.dynamic_obstacles)):
            dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
            new_x = self.dynamic_obstacles[i][0] + dx
            new_y = self.dynamic_obstacles[i][1] + dy
            new_pos = [max(0, min(new_x, GRID_WIDTH - 1)), max(0, min(new_y, GRID_HEIGHT - 1))]

            if new_pos != self.agent_pos and new_pos != self.goal_pos and new_pos not in self.obstacles and new_pos not in self.dynamic_obstacles:
                self.dynamic_obstacles[i] = new_pos

    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_LINE_COLOR, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRID_LINE_COLOR, (0, y), (WINDOW_WIDTH, y))

    def draw_objects(self):
        for obs in self.obstacles + self.dynamic_obstacles:
            pygame.draw.rect(self.screen, OBSTACLE_COLOR,
                             (obs[0]*CELL_SIZE, obs[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(self.screen, GOAL_COLOR,
                         (self.goal_pos[0]*CELL_SIZE, self.goal_pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(self.screen, AGENT_COLOR,
                         (self.agent_pos[0]*CELL_SIZE, self.agent_pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def render(self):
        self.update_dynamic_obstacles()
        self.screen.fill(WHITE)
        self.draw_grid()
        self.draw_objects()
        pygame.display.flip()
        self.clock.tick(30)