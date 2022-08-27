#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 5

Created on Thu Aug 25 14:33:53 2022

@author: Alma Velazquez
"""

###### Given code ##############################
class Node:
    def __init__(self, _value=None, _next=None):
        """Constructor for class Node. Default value and next
        attributes set to None. """

        self.value = _value
        self.next = _next

    def __str__(self):
        """String representation of a class Node oject is its
        value attribute."""

        return str(self.value)

    #####################################################

    def delNode(self, target):
        """Searches all parent and children nodes for target matches.
        Helper function for LinkedList.removeNodeByValue() method. """

        # perform the following until there are no next nodes
        while self.next != None:

            # if the value of present node matches the target,
            if self.value == target:

                # call method recursively on the next node, leaving off the current one
                return self.next.delNode(target)

            else:
                # otherwise return a new node including the current node and its next attribute
                return Node(self.value, self.next.delNode(target))


class LinkedList:
    def __init__(self):
        """Constructor for class LinkedList. Instantiates a default head value
        of None. """

        self.head = None

    def addNode(self, new_value):
        """Adds a Node object of given value to the end of LinkedList
        objects. """

        # if a head node exists,
        if self.head != None:

            # set it as the starting value,
            last_node = self.head

            # traverse over its children until last node reached
            while last_node.next != None:

                last_node = last_node.next

            # set next attribute of last node to new node
            last_node.next = Node(new_value)

        else:
            # if no head node exists, assign this node to it
            self.head = Node(new_value)

    def __str__(self):
        """String representation of a class LinkedList oject is a string
        of its node values separated by pointers, with the last one
        pointing at a Null object. """

        # set starting current node as head node
        curr_node = self.head

        # instantiate empty string
        string = ""

        # traverse node children until there is no next node
        while curr_node != None:

            # add node value and pointer to string
            string += str(curr_node.value) + " --> "

            # advance to next node
            curr_node = curr_node.next

        # represent the Null value at end of LinkedList
        string += "Null"

        # return concatenated values
        return string

    def getNode(self, position):
        """"Traverse LinkedList to return node at the desired 
        position, indexed from 0. Helper function for several 
        methods of class LinkedList. """ ""

        # this error will surface in addNodeAfter if non-integer node position passed
        if not isinstance(position, int):
            raise TypeError("node must be indexed with an integer.")

        # set starting current node as head node
        curr_node = self.head

        # advance over child nodes until desired position reached
        for i in range(position):

            curr_node = curr_node.next

        # return the node at that position
        return curr_node

    def addNodeAfter(self, new_value, after_node):
        """Inserts a new node of given value after the position indicated, 
        indexed from 0."""

        # traverse the necessary number of nodes to get the after_node
        curr_node = self.getNode(after_node)

        # create a new node,
        new_node = Node(new_value)

        # whose .next will be everything that comes after the after_node
        new_node.next = curr_node.next

        # the after_node's .next is the new node's .next (everything we just appended after it)
        curr_node.next = new_node

    def addNodeBefore(self, new_value, before_node):
        """Inserts a new node of given value before the position indicated, 
        indexed from 0."""

        # raise informative error instead of "unsupported operand"
        if not isinstance(before_node, int):
            raise TypeError("node must be indexed with an integer.")

        # create a new node
        new_node = Node(new_value)

        # address this unique case
        if before_node == 0:

            new_node.next = self.head

            self.head = new_node

        else:
            # need the node before the before_node, to reassign its .next
            prev_node = self.getNode(before_node - 1)

            # the before_node will be this node's .next
            curr_node = prev_node.next

            # assign the .next of the new node to be the current node
            new_node.next = curr_node

            # the node before the before_node's .next is now the new node, front-appended to the before_node
            prev_node.next = new_node

    def removeNode(self, node_to_remove):
        """Remove the node at the indicated position. """

        # address this unique case
        if node_to_remove == 0:

            self.head = self.head.next

        else:
            # need the node before the node desired for removal
            prev_node = self.getNode(node_to_remove - 1)

            # assign its .next as the current node
            curr_node = prev_node.next

            # assign to the .next of the previous node the .next of node to remove, so everything after it is kept
            prev_node.next = curr_node.next

            # nullify
            curr_node = None

    def removeNodesByValue(self, value):
        """"Remove all nodes whose values match the target value given. """ ""

        # call the delNode method on the head node, which traverses all its children looking for matches; reassign head node
        self.head = self.head.delNode(value)

    def length(self):
        """Return current length of the LinkedList object. """

        # set start value of current node to be the head node
        curr_node = self.head

        # start the counter at 1
        counter = 1

        # until there is no next node,
        while curr_node.next != None:

            # advance to the next node
            curr_node = curr_node.next

            # increment counter
            counter += 1

        # assign end counter value to length attribute
        self.length = counter

        # return end counter value
        return counter

    def reverse(self):
        """Reverses the node order of a LinkedList object. """
        # instantiate empty previous node
        prev_node = None

        # start value of current node is head node
        curr_node = self.head

        # until there is no next node,
        while curr_node != None:

            # create a "next node" that has everything after current node
            next_node = curr_node.next

            # assign everything after the current node to be previous node
            curr_node.next = prev_node

            # now advance previous node to current
            prev_node = curr_node

            # advance current node to next node
            curr_node = next_node

        # assign the ending previous node to the head of LinkedList
        self.head = prev_node


## tests
ll1 = LinkedList()
ll1.addNode("h")
ll1.addNode(9)
ll1.addNode(11)
ll1.addNode(16)
ll1.addNode(16)
ll1.addNode(5)
ll1.addNode(18)

print(ll1)
ll1.length()

# uncomment to test error handling
# ll1.addNodeBefore(7, "y")
# ll1.addNodeAfter(7, "h")


ll1.addNodeBefore(7, 0)
ll1.addNodeBefore(12, 1)
ll1.addNodeAfter(9, 0)

ll1.removeNode(0)
print(ll1)


ll1.removeNodesByValue(7)
ll1.removeNodesByValue(16)
ll1.removeNodesByValue("h")

ll1.reverse()
