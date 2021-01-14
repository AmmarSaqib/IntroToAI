
import heapq

class PriorityQueue:

    """
    The class provides an implementation of priority queses via min heaps. This class has basic functions of a priority queue.
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
        and returns the item along with the cost of it.

        :return : the item with the lowest priority
        """

        temp = heapq.heappop(self.__queue)
        
        cost = temp[0]
        item = temp[-1]

        return cost, item

    def is_empty(self):
        """
        Checks whether the queue is empty or not.

        :returns: (Boolean)
        """
        return len(self.__queue) == 0
    
if __name__ == "__main__":
    
    # testing priority queue
    queue = PriorityQueue()
    queue.insert('e', 9)
    queue.insert('a', 2)
    queue.insert('h', 13)
    queue.insert('c', 11)
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())