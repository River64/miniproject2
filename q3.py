# Luis Hernandez, River Johnson
# This code was partially generated by AI (OpenAI ChatGPT)

import networkx as nx
import random
import matplotlib.pyplot as plt

def simulate_cover_time(N, C, trials=1000):
    successful_trials = 0
    total_steps = 0
    connected_count = 0

    for _ in range(trials):
        g = nx.gnm_random_graph(N, C)
        if not nx.is_connected(g):
            continue  # skip disconnected graphs

        connected_count += 1
        current = random.choice(list(g.nodes))
        visited = {current}
        steps = 0

        while len(visited) < N and steps < 1000:
            neighbors = list(g.neighbors(current))
            current = random.choice(neighbors)
            visited.add(current)
            steps += 1

        total_steps += steps
        successful_trials += 1

    avg_time = total_steps / successful_trials if successful_trials > 0 else None
    connectivity = connected_count / trials
    return avg_time, connectivity

# === Run experiment ===
N = 20
C_range = list(range(N - 1, min(81, (N * (N - 1)) // 2 + 1), 5))  # from minimal to dense, capped at 80 for best view
cover_times = []
connectivities = []

for C in C_range:
    avg_time, connectivity = simulate_cover_time(N, C, trials=50)
    cover_times.append(avg_time)
    connectivities.append(connectivity)

# === Plot results ===
fig, ax1 = plt.subplots(figsize=(10,5))

color = 'tab:blue'
ax1.set_xlabel('Number of Edges (C)')
ax1.set_ylabel('Average Cover Time', color=color)
ax1.plot(C_range, cover_times, color=color, label='Avg Cover Time')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Connectivity Rate', color=color)
ax2.plot(C_range, connectivities, color=color, linestyle='--', label='Connectivity %')
ax2.tick_params(axis='y', labelcolor=color)

plt.title(f"Effect of Lowering C on Cover Time and Connectivity (N={N})")
fig.tight_layout()
plt.show()
