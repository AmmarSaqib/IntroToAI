"""
Lab Task: 

For this lab you will be implementing Uniform Cost Search on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable 
with the functions

MAIN TASK:
The graph provided has already been created below and the UCS (Unifrom cost search) function has been called.
You are suppose to fill in the UCS function declared below. A description of what the function should do is mentioned.
Use functions from the helper classes in order to write the UCS function.
Your function should print the shortest path along with the cost of that path. 
A sample output is provided in the assests directory.
"""

# importing helper classes
from graph import Graph
from queue import PriorityQueue

def uniform_cost_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according 
    to the Uniform Cost Search Algorithm.

    NOTE: print the path and cost

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graph
    :params goal_node: (String) goal node from the graph

    :return : None
    """

    # write your code below

    pass # remove this line when coding

if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {
        'A': set(['B', 'D']),
        'B': set(['A','E','C']),
        'C': set(['B', 'E', 'G']),
        'D': set(['A','E','F']),
        'E': set(['B', 'C', 'D', 'G']),
        'F': set(['D','G']),
        'G': set(['F','E','C'])
    }

    # setting up connection costs
    graph.weights = {
        'AB': 5, 'AD': 3,
        'BA': 5, 'BE': 4, 'BC': 1,
        'CB': 1, 'CE': 6, 'CG': 8,
        'DA': 3, 'DE': 2, 'DF': 2,
        'EB': 4, 'EC': 6, 'ED': 2, 'EG': 4,
        'FD': 2, 'FG': 3,
        'GF': 3, 'GE': 4, 'GC': 8
    }

    uniform_cost_search(graph, 'A', 'G') 
    """
    the above statement should result in the following:
    
    Shortest Path: A,D,F,G
    Cost: 8
    """