import networkx as nx
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

def generate_connected_graph(N, C):
    while True:
        G = nx.gnm_random_graph(N, C)
        if nx.is_connected(G):
            return G

def random_walk_cover_time(G, start=None):
    visited = set()
    if start is None:
        start = random.choice(list(G.nodes()))
    current = start
    steps = 0

    while len(visited) < len(G.nodes()):
        visited.add(current)
        neighbors = list(G.neighbors(current))
        if not neighbors:
            break  # shouldn't happen if G is connected
        current = random.choice(neighbors)
        steps += 1

    return steps

def average_cover_time(N, C, trials=100):
    times = []
    for _ in tqdm(range(trials)):
        G = generate_connected_graph(N, C)
        t = random_walk_cover_time(G)
        times.append(t)
    return sum(times) / len(times)

# Example test
N = 10
C = 15
avg_time = average_cover_time(N, C, trials=100)
print(f"Average cover time for N={N}, C={C}: {avg_time:.2f} steps")
