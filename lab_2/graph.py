
class Graph:
    """
    The purpose of the class is to provide a clean way to define a graph for
    a searching algorithm:
    """

    def __init__(self):
        self.edges = {} # dictionary of edges NODE: NEIGHBOURS
        self.weights = {} # dictionary of NODES and their COSTS

    def neighbours(self, node):
        """
        The function returns the neighbour of the node passed to it,
        which is essentially the value of the key in the edges dictionary.

        :params node: (string) a node in the graph

        :return: (list) neighbouring nodes
        """

        return self.edges[node]

    def get_cost(self, from_node, to_node):
        """
        Gets the cost of a connection between adjacent nodes.

        :params from_node: (string) starting node
        :params to_node: (string) ending node

        :return: (int) 
        """
        
        return self.weights[(from_node + to_node)]



if __name__ == "__main__":
    # testing out the graph class
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

    print("Neighbours of Node A are:",graph.neighbours('A'))
    print("Cost going from A to D is:", graph.get_cost('A','D'))