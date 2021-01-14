"""
Lab: 1
Task: B

Your task is to implement a basic Priority Queue, using Arrays, in python in an OOP fashion.
Priority Queue is an extension of queue with following properties:
    -> Every item has a priority associated with it.
    -> An element with high priority is dequeued before an element with low priority.
    -> If two elements have the same priority, they are served according to their order in the queue.


You Priority Queue should have the following functions working for it:
    -> insert(item, priority): Inserts an item with fiven priority.
    -> get_highest_priority(): Returns the highest priority item.
    -> delete_highest_priority(): Removes the highest priority item.

Fill in the boiler plate class in this file.
You may create helper function to assist you for this task.

(NOTE: you are not allowed to to use libraries for this Task)
"""

class PriorityQueue():

    def __init__(self):
        self.queue = [] # list to hold items in a priority queue manner

    def insert(self, value, priority):
        """
        Inserts the value along with the priority in the queue.
        The value and priority should be inserted as a tuple (value, priority) in the queue.

        :param value: (any datatype) value to be inserted
        :param priority: (int) priority number associated with the value

        :return: None
        """

        item = (value, priority) # creating a tuple of item with value and priority

        # enter your code below
        pass # remove this line once you start filling in the code

    def get_highest_priority(self):
        """
        Search of the highest priority item and return the value with
        the highest priority.

        NOTE: if the priorities are same for certain values, return the 
        value that was inserted first.

        :return: value with highest priority
        """

        # enter your code below
        pass # remove this line once you start filling in the code

    def delete_highest_priority(self):
        """
        Delete the item with the highest priority.

        NOTE: if the priorities are same for certain values, remove the 
        value that was inserted first.

        :return: None
        """

        # enter your code below
        pass # remove this line once you start filling in the code

    ######## Helper functions below ################




    ################################################

if __name__ == "__main__":
    """
    check your priority queue by inserting some values in it and then dequeue them
    and see whether your results follow the FIFO (First In First Out)
    """

    # enter your code below
    pass # remove this line once you start filling in the code