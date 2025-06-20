from pylab import *
import networkx as nx
import random

def initialize(n, c):
    global graph, cnode, walk_result
    # Generate random connected graph with N nodes and C edges
    attempting = True
    while attempting:
        graph = nx.gnm_random_graph(n, c)
        if nx.is_connected(graph):
            attempting = False
    
    # Set the starting node- "first" is random, because the graph is randomly generated
    cnode = list(graph.nodes)[0]
    # Add the starting node to the time series
    walk_result = [cnode]

def observe():
    # Add the new current node to the result
    global walk_result, cnode
    walk_result.append(cnode)

def update():
    global cnode, graph
    # Choose a random next node to visit from current node's neighbors
    neighbors = list(graph.neighbors(cnode))
    cnode = random.choice(neighbors)

# Returns true if all nodes in the graph have been visited by the walker
# Checked during simulation
def all_visited():
    global graph, walk_result
    result = len(set(walk_result)) == graph.number_of_nodes()
    # So that the simulation doesn't run forever:
    if (walk_result.__len__() > 100):
        result = True
    return result

time_for_average = []
# Simulate this walking 100 times
for i in range(100):
    initialize(10, 50)
    while(not all_visited()):
        update()
        observe()
    # print(walk_result)
    time_for_average.append(walk_result.__len__())
# Calculate and print average walking time:
print("Average walking time:", sum(time_for_average) / time_for_average.__len__())