"""
Lab Task: 
"""

# importing helper classes
from graph import Graph
from queue import PriorityQueue

def uniform_cost_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according 
    to the Uniform Cost Search Algorithm.

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graph
    :params goal_node: (String) goal node from the graph

    :return : None
    """

    visited = []
    queue = PriorityQueue()
    queue.insert(start_node, 0)
    total_cost = 0

    while not queue.is_empty():
        temp = []
        cost, node = queue.remove()
        # print(node)

        if node not in visited:
            visited.append(node)

            if node[-1] == goal_node:
                break

            for i in graph.neighbours(node[-1]):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node[-1], i)
                    queue.insert(node + ',' + i, total_cost)

    print("Shortest Path:", node)
    print("Cost:", cost)


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