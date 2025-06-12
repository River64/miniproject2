import networkx as nx
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

# Generate a connected random graph with N nodes and C edges
def generate_connected_graph(N, C):
    while True:
        G = nx.gnm_random_graph(N, C)
        if nx.is_connected(G):
            return G

# Visualize the graph with visited nodes highlighted
def draw_graph(G, visited, step=None):
    color_map = ['red' if node in visited else 'lightgray' for node in G.nodes()]
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6, 5))
    if step is not None:
        plt.title(f"Random Walk - Step {step}")
    else:
        plt.title("Final Walk State")
    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=500, edge_color='gray')
    plt.show()

# Run a random walk and return steps to cover all nodes (optional visualization)
def random_walk_cover_time(G, start=None, visualize=False):
    visited = set()
    if start is None:
        start = random.choice(list(G.nodes()))
    current = start
    steps = 0

    if visualize:
        draw_graph(G, visited, step=0)

    while len(visited) < len(G.nodes()):
        visited.add(current)
        if visualize and steps % 5 == 0:  # draw every few steps for speed
            draw_graph(G, visited, step=steps)

        neighbors = list(G.neighbors(current))
        if not neighbors:
            break
        current = random.choice(neighbors)
        steps += 1

    if visualize:
        draw_graph(G, visited)

    return steps

# Run multiple trials and report average cover time
def average_cover_time(N, C, trials=100, show_first_trial=False):
    times = []
    for i in tqdm(range(trials)):
        G = generate_connected_graph(N, C)
        if show_first_trial and i == 0:
            print(f"Visualizing first trial (N={N}, C={C})...")
            t = random_walk_cover_time(G, visualize=True)
        else:
            t = random_walk_cover_time(G)
        times.append(t)
    return sum(times) / len(times)

# -------------------------------
# Example Usage
# -------------------------------
N = 10
C = 15
avg_time = average_cover_time(N, C, trials=100, show_first_trial=True)
print(f"\nAverage cover time for N={N}, C={C}: {avg_time:.2f} steps")
