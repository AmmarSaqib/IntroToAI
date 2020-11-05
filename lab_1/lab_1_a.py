"""
Lab: 1
Task: A

Your task is to implement a basic Queue in python in an OOP fashion.
Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

You Queue should have the following functions working for it:
    -> Enqueue(item): Adds an item to the queue.
    -> Dequeue(): Removes an item form the queue. The items are popped in the same order in whcih they are pushed
    -> Front(): Get the fron item from queue.
    -> Rear(): Get the last item from the queue.

Fill in the boiler plate class in this file.
You may create helper function to assist you for this task.

(NOTE: you are not allowed to to use libraries for this Task)
"""

class Queue():

    def __init__(self):
        self.queue = [] # list to hold the elements

    def enqueue(self, value):
        """
        Add the value to the list.

        :param value: (any datatype) the value to be inserted into the queue

        return: None
        """

        # enter your code below
        pass # remove this line once you start filling in the code

    def dequeue(self):
        """
        Remove and return the item from the list.

        :return: value from the queue
        """

        # enter your code below
        pass # remove this line once you start filling in the code

    def front(self):
        """
        Get the front item form the queue.

        :return: front element from queue
        """

        # enter your code below
        pass # remove this line once you start filling in the code

    def rear(self):
        """
        Get the last item form the queue.

        :return: last element from queue
        """

        # enter your code below
        pass # remove this line once you start filling in the code

    ######## Helper functions below ################




    ################################################

if __name__ == "__main__":
    """
    check your queue by inserting some values in it and then dequeue them
    and see whether your results follow the FIFO (First In First Out)
    """

    # enter your code below
    pass # remove this line once you start filling in the code