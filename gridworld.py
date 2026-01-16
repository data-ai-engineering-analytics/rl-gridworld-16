import numpy as np

# ==========================================
# 1. CONFIGURATION
# ==========================================
# Grid size
N = 4
num_states = N * N

# Terminal state index (bottom-right corner)
terminal_state = num_states - 1

# Discount factor and convergence threshold
gamma = 1.0
theta = 1e-4

# Initialize value function
V = np.zeros(num_states)

# ==========================================
# 2. ENVIRONMENT DYNAMICS
# Actions: up, down, left, right
actions = {
    "up":    (-1,  0),
    "down":  ( 1,  0),
    "left":  ( 0, -1),
    "right": ( 0,  1)
    }

# Helper function to get next state given current state and action
def next_state(state, action):
    row = state // N
    col = state % N

    dr, dc = action
    new_row = row + dr
    new_col = col + dc

    # Check boundaries
    if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
        return state  # stay in same state
    else:
        return new_row * N + new_col


if __name__ == "__main__":
    print("main")
    while True:
        delta = 0
        V_new = V.copy()

        for s in range(num_states):
            # Skip terminal state
            if s == terminal_state:
                continue

            value = 0.0

            # Bellman expectation update
            for action in actions.values():
                s_next = next_state(s, action)
                reward = -1
                value += 0.25 * (reward + gamma * V[s_next])

            V_new[s] = value
            delta = max(delta, abs(V_new[s] - V[s]))

        V = V_new

        if delta < theta:
            break

    # Reshape into 4x4 grid for readability
    V_grid = V.reshape(N, N)
    print(V_grid)