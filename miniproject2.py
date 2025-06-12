from pylab import *
import networkx as nx

def initialize(n, c):
    global graph, cnode, walk_result
    # Generate random graph with N nodes and C edges
    graph = nx.gnm_random_graph(n, c)
    # Set all nodes to be unvisited
    nx.set_node_attributes(graph, 0, name = "visited")
    # Set the starting node- "first" is random, because the graph is randomly generated
    cnode = graph.nodes.first()
    # Add the starting node to the time series
    walk_result = [cnode]

def observe():
    # Add the new current node to the result
    global walk_result, cnode
    walk_result.append(cnode)

def update():
    cnode.visited = 1
    # choose a random edge from cnode
    # Set the node on the other side of that edge as the current node

# Returns true if all nodes in the graph have been visited by the walker
def all_visited():
    global graph
    result = true
    for node in graph.nodes:
        result = result & (node.visited == 1)
    return result