# RL GridWorld Simulator

This project implements a **Reinforcement Learning (RL) GridWorld Simulator** where an agent learns to navigate a grid-based environment using the Bellman equation. The agent starts at the top-left corner and aims to reach the bottom-right corner while minimizing penalties for each move.

---

## Features

- **GridWorld Environment**:
  - Configurable grid size (default: 4x4).
  - Agent starts at the top-left corner and aims to reach the bottom-right corner.
  - Rewards:
    - `-1` for each move.
    - `0` for reaching the terminal state (goal).
  - No obstacles in the environment.

- **Bellman Equation Implementation**:
  - Iteratively applies the Bellman equation to compute the value function for each state.
  - Stops when the maximum change in the value function across all states is below a defined threshold.

---

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rl-gridworld-simulator.git
   cd rl-gridworld-simulator
   ```

2. (Optional) If you are using a virtual environment, activate it:
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

---

## How to Run

1. Start the simulator:
   ```bash
   python gridworld.py
   ```

2. The program will:
   - Initialize the grid and value function.
   - Iteratively apply the Bellman equation until convergence.
   - Print the final value function.

---

## Bellman Equation Implementation

The Bellman equation is iteratively applied to compute the value function for each state until convergence. The process is as follows:

1. **Initialization**:
   - Set grid size (NxN).
   - Define rewards for each state (`-1` per move, `0` for the terminal state).
   - Initialize the value function `V(s) = 0` for all states.
   - Set the discount factor (`gamma = 1`) and convergence threshold (`theta = 1e-4`).

2. **Value Iteration**:
   - For each state `s` (excluding the terminal state):
     - Compute the new value using the Bellman equation:
       - For each action, calculate:
         - Next state `s'` (handling grid boundaries).
         - Expected value update: sum over all possible `s'`.
     - Update `V(s)`.

3. **Convergence**:
   - Stop when the maximum change in `V(s)` across all states is less than the threshold.

---

## Example Output

The final value function after convergence might look like this:

```
[[-59.42 -57.42 -54.28 -51.71]
 [-57.42 -54.56 -49.71 -45.13]
 [-54.28 -49.71 -40.85 -29.99]
 [-51.71 -45.13 -29.99   0.  ]]
```

---

## File Structure

```
rl-gridworld-16/
├── LICENSE
├── gridworld.py
├── pyproject.toml
├── README.md
└── __pycache__/
```

---

## References

- [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 