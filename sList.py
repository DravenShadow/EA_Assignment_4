"""
            sList.py                            Author: Rowland DePree

            Two classes to allow the creation of a singular linked list.

"""


class Node:
    """
    A class to create a node.  The original form of this code is from the Essential Algorithms course at
    Harrisburg University of Science & Technology.
    """

    def __init__(self, data, next_node):
        """

        :param data
        :param next_node
        :return None
        """
        self.data = data
        self.next = next_node


class sList:
    """
    A class to create a singular linked list.  The original form of this code is from the Essential Algorithms course at
    Harrisburg University of Science & Technology.
    """

    def __init__(self):
        """
        Constructor

        :return None
        """
        self.head_node = None
        self.size = 0

    def __str__(self):
        """
        Overwrites the str method to work better for a linked list.

        :return ' ,'.join(output)
        """
        output = []
        curr = self.head_node
        while curr is not None:
            output.append(str(curr.data, ))
            curr = curr.next
        return ' ,'.join(output)

    def add_Front(self, data):
        """
        Adds a node to the front of the linked list

        :param data
        :return None
        """
        self.head_node = Node(data, self.head_node)
        self.size += 1

    def remove(self, data):
        """"
        Removes a node from the linked list based upon the data given to it.

        :param data
        :return True
        :return False
        """
        if self.size == 0:
            return False
        elif self.head_node.data == data:
            self.head_node = self.head_node.next
            self.size -= 1
            return True
        else:
            curr = self.head_node
            while curr.next is not None and curr.next.data != data:
                curr = curr.next
            if curr.next is None:
                return False
            else:
                curr.next = curr.next.next
                self.size -= 1
                return True
