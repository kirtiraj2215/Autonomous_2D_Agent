# 2D Autonomous Agent (Reinforcement Learning Approach)

## Objective
The objective of this project is to build a basic autonomous agent that can navigate a 2D grid environment using **Reinforcement Learning (RL)**. The agent starts from a fixed starting point, avoids obstacles (both static and dynamic), and reaches the goal point. This project simulates the core concepts of autonomous systems such as navigation, perception, and decision-making in a simple 2D virtual environment, which helps in understanding the principles behind real-world autonomous systems.

## Libraries & Tools

- **Programming Language**: Python
- **Libraries Used**:
  - **Pygame**: For creating the 2D environment and visualizing the agent's movements.
  - **Numpy**: For numerical calculations and managing Q-table data structures.
  - **CSV**: For logging performance data (e.g., rewards, time taken, steps, and collisions).
  
- **Machine Learning Approach**:
  - **Reinforcement Learning (RL)** using **Q-learning** algorithm for decision-making.

## Project Structure

vyorius_rl/
├── env.py               ← Contains the grid environment and agent definition.
├── main.py              ← Main code for training the agent with Q-learning.
├── performance_log.csv  ← Auto-generated file to log performance metrics.
├── README.md            ← Project description and setup instructions.

## Setup Instructions

### Prerequisites

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download this repository to your local machine.

### Installation

1. Install the required libraries:
   
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv

Activate the virtual environment:
	•	On Windows:
 
```bash
venv\Scripts\activate


	•	On macOS/Linux:

```bash
source venv/bin/activate



	2.	Install the dependencies:

```bash
pip install pygame numpy



Running the Simulation
	1.	Once all dependencies are installed, you can run the simulation using the following command:

```bash
python main.py


	2.	The program will start the simulation, where the agent will begin at a starting point and attempt to reach the goal while avoiding obstacles. During the training, the agent will gradually improve its navigation abilities through reinforcement learning.

Explanation of Approach

1. Reinforcement Learning (Q-learning)

We implemented Q-learning, a model-free reinforcement learning algorithm that allows the agent to learn optimal actions from interactions with the environment. The main components of the Q-learning algorithm are:
	•	States: Represent the agent’s current position in the 2D grid.
	•	Actions: The possible actions that the agent can take: move up, down, left, or right.
	•	Q-values: A table that stores the expected future rewards for each state-action pair. The Q-values are updated based on the agent’s experience.
	•	Rewards: The feedback the agent receives after taking an action. In this case:
	•	A reward of ( +100 ) when the agent reaches the goal.
	•	A penalty of ( -10 ) when the agent collides with an obstacle.
	•	A penalty of ( -1 ) for each step taken to encourage efficient navigation.

The agent updates its Q-values based on the Bellman equation, which helps it learn the optimal policy (i.e., the best actions to take for each state). The agent uses an epsilon-greedy policy to balance exploration (random actions) and exploitation (using the best-known actions from the Q-table).

2. Dynamic Obstacles

The environment includes both static and dynamic obstacles:
	•	Static Obstacles: These are placed in fixed locations on the grid and cannot be moved by the agent.
	•	Dynamic Obstacles: These move randomly during the simulation, adding a layer of complexity to the agent’s navigation. The agent must adjust its behavior to account for these obstacles.

3. Agent’s Movement and Learning Process

The agent starts at a random position and attempts to reach the goal. During each episode:
	•	The agent selects an action (up, down, left, or right) using the epsilon-greedy policy.
	•	The agent moves to a new state, receives a reward, and updates its Q-values based on the Bellman equation.
	•	The exploration rate ( \epsilon ) decays over time, so the agent explores more at the beginning and gradually exploits its learned knowledge more as training progresses.

The environment, agent movements, and obstacles are visualized using Pygame. The simulation updates in real-time, showing the agent’s movements, rewards, and collisions.

4. Performance Logging

Throughout the training process, we log key performance metrics in a CSV file:
	•	Episode Number: The current training episode.
	•	Total Reward: The sum of all rewards the agent received in the episode.
	•	Time Taken: The total time taken for the agent to complete the episode.
	•	Steps Taken: The number of steps the agent took in the episode.
	•	Collisions: The number of times the agent collided with an obstacle.
	•	Epsilon: The exploration rate used during the episode.

This data can be used for analysis to understand how the agent’s performance improves over time.

Example Log:

```bash
Episode, Reward, Time(s), Steps, Collisions, Epsilon
1, 50, 1.25, 30, 3, 0.995
2, 80, 1.10, 35, 1, 0.990
3, 90, 1.05, 32, 2, 0.985

Challenges Faced

1. Dynamic Obstacles Handling

One of the biggest challenges was implementing dynamic obstacles that move during the simulation. This required careful tracking of obstacle positions and ensuring that the agent could detect and avoid them in real-time. The challenge was exacerbated when obstacles moved unpredictably.

2. Balancing Exploration and Exploitation

During training, the agent initially explored the environment too much, which led to slow learning. Balancing the exploration rate ( \epsilon ) was critical to achieving optimal performance. We experimented with different decay rates for ( \epsilon ) to find an appropriate balance between exploration and exploitation.

3. Real-time Performance Monitoring

Tracking performance metrics such as time, collisions, and steps in real-time without interfering with the gameplay was challenging. We used CSV logging to record these metrics for each episode and visualize the agent’s progress over time.

Ideas for Improvement

1. Deep Q-Networks (DQN)

Currently, the agent uses a Q-table, which is efficient for small state spaces. However, as the environment grows in complexity, the Q-table becomes less effective. Implementing Deep Q-Networks (DQN), where a neural network approximates the Q-values, would allow the agent to handle larger state spaces and generalize to new situations.

2. Multi-Agent Systems

Introducing multiple agents could simulate scenarios where agents need to cooperate or compete for resources. This could provide interesting insights into learning in multi-agent environments.

3. Dynamic Difficulty Adjustment

To improve the training experience, we could adjust the environment’s difficulty dynamically based on the agent’s performance. For example, increasing the number of obstacles or the speed of dynamic obstacles as the agent becomes more proficient could help accelerate learning and prevent the agent from reaching a plateau.

4. Better Obstacle Generation

The current obstacles are simple rectangular blocks. Future improvements could include more complex obstacles with varying shapes and movement patterns, making the environment more realistic and challenging.

Conclusion

This project successfully demonstrates how a Q-learning agent can navigate a 2D environment, avoid obstacles, and reach a goal. By applying reinforcement learning, the agent learns to optimize its behavior through trial and error. The challenges of dynamic obstacles and balancing exploration and exploitation were addressed, and the agent’s performance improved over time. Future improvements could include using Deep Q-Networks, multi-agent systems, and dynamic difficulty adjustments to make the environment more complex and realistic.

Acknowledgements

Special thanks to the Python community for libraries like Pygame and NumPy, which made building this simulation much easier.

---

This detailed README includes all necessary setup instructions, an explanation of the approach, challenges faced, and ideas for improvement. Let me know if you'd like further modifications or additions!
