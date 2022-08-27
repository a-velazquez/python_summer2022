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

        # if no head node exists, assign this node to it
        else:

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

        # set starting current node as head node
        curr_node = self.head

        # advance over child nodes until desired position reached
        for i in range(position):

            curr_node = curr_node.next

        # return the node at that position
        return curr_node

    def addNodeAfter(self, new_value, after_node):

        # traverse the necessary number of nodes to get the after_node
        curr_node = self.getNode(after_node)

        # create a new node
        new_node = Node(new_value)

        # whose next will be everything that comes after the after_node
        new_node.next = curr_node.next

        # the after_node's next is the new node's next (everything we just appended after it)
        curr_node.next = new_node

    def addNodeBefore(self, new_value, before_node):

        # need the node before the before_node, to reassign its .next
        prev_node = self.getNode(before_node - 1)

        # the before_node will be this node's .next
        curr_node = prev_node.next

        # create a new node
        new_node = Node(new_value)

        new_node.next = curr_node

        prev_node.next = new_node

    def removeNode(self, node_to_remove):

        prev_node = self.getNode(node_to_remove - 1)

        curr_node = prev_node.next

        prev_node.next = curr_node.next

        curr_node = None

    def removeNodesByValue(self, value):
        """". """ ""

        self.head = self.head.delNode(value)

    def length(self):

        curr_node = self.head
        counter = 1

        while curr_node.next != None:

            curr_node = curr_node.next
            counter += 1

        self.length = counter

        return counter

    def reverse(self):

        prev_node = None

        curr_node = self.head

        while curr_node != None:

            next_node = curr_node.next

            curr_node.next = prev_node

            prev_node = curr_node

            curr_node = next_node

        self.head = prev_node


ll1 = LinkedList()
node0 = ll1.addNode(6)
node1 = ll1.addNode(9)
node2 = ll1.addNode(11)
node3 = ll1.addNode(16)
ll1.addNode(16)
ll1.addNode(16)
ll1.addNode(16)

print(ll1)
ll1.length()

ll1.addNodeBefore(7, 2)
ll1.addNodeAfter(7, 2)

ll1.removeNode(4)

ll1.removeNodesByValue(7)
ll1.removeNodesByValue(16)

ll1.reverse()
