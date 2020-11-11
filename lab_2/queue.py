
import heapq

class PriorityQueue:

    """
    The class provides an implementation of priority queses via min heaps. This class has basic interation functions.
    """

    def __init__(self):
        self.__queue = []
        self.__index = 0

    def insert(self, item, priority):
        """
        The function takes in the item and its priority, wraps it up in a tuple and 
        inserts it in the heap.

        :params item: item to be inserted into the queue
        :params priority: the priority of the item to be inserted

        :return: None
        """

        heapq.heappush(self.__queue, (priority, self.__index, item))
        self.__index += 1

    def remove(self):
        """
        The functions removes the lowest priority item from the priority queue (via heaps)
        and returns it.

        :return : the item with the lowest priority
        """
    
        return heapq.heappop(self.__queue)[-1]

    def is_empty(self):
        """
        Checks whether the queue is empty or not.

        :returns: (Boolean)
        """
        return len(self.__queue) == 0
    