"""
Lab Task: 

For this lab you will be implementing A* (A Star Search) on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable 
with the functions

MAIN TASKS:

    1- Modify graph.py to have the ability to store heuristics
    2- Create a funciton 'get_h' in graph.py to get heuristic for a node
    3- Create the graph in graph.py to and check all the functions
    4- Replicate the graph in 'lab_3.py'
    5- Implement A* function 

Your function should print the shortest path along with the cost of that path. 
A sample output is provided in the assests directory.
"""

# importing helper classes
from graph import Graph
from queue import PriorityQueue

def a_star_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according 
    to the A* Search Algorithm.

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

    # setting up connection costs

    a_star_search(graph, 'S', 'G') 