from pylab import *
import networkx as nx

def initialize(n, c):
    global graph, cnode, walk_result
    # Generate random graph with N nodes and C edges
    graph = nx.gnm_random_graph(n, c)
    # Set all nodes to be unvisited
    nx.set_node_attributes(graph, False, name = "visited")
    # Set the starting node- "first" is random, because the graph is randomly generated
    cnode = graph.nodes.first()
    # Add the starting node to the time series
    walk_result = [cnode]

def observe():
    # Add the new current node to the result
    global walk_result, cnode
    walk_result.append(cnode)

def update():
    # Set our current node as visited
    cnode.visited = True
    # Choose a random next node to visit from current node's neighbors
    cnode = random.choice(cnode.nodes)

# Returns true if all nodes in the graph have been visited by the walker
# Checked during simulation
def all_visited():
    global graph, walk_result
    result = True
    for node in graph.nodes:
        result = result & node.visited
    # So that the simulation doesn't run forever:
    if (walk_result.__len__ > 100):
        result = True
    return result

time_for_average = []
# Simulate this walking 15 times
for i in range(15):
    initialize(10, 10)
    while(not all_visited()):
        update()
        observe()
    print(walk_result, end = "\n\n")
    time_for_average.append(walk_result.__len__)
# Calculate and print average walking time:
print("Average walking time:", sum(time_for_average) / 15)