#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 4

Created on Tue Aug 23 16:44:36 2022

@author: Alma Velazquez
"""

import matplotlib.pyplot as plt
import time
from random import randint

# make an input list to test the sorting algorithms with
input_arr = [3, 4, 5, 6, 2, 1]

#### Tree Sort
### Reference:

## define helper functions
def insert(tree, k):
    """Adds node to binary search tree,
    in which nodes less than the root are on the left,
    and nodes greater than the root are on the right."""

    # if tree is empty
    if tree == None:
        # instantiate new tree and return
        tree = {"root": k, "left": None, "right": None}
        return tree

    # if node is less than tree's root, recursively add to the left node
    if k < tree["root"]:
        tree["left"] = insert(tree["left"], k)

    # if node is greater than tree's root, recursively add to the right node
    elif k > tree["root"]:
        tree["right"] = insert(tree["right"], k)

    # return tree
    return tree


def traverse(tree, sorted_array=[]):
    """Traverses binary search tree in order from left to right,
    returns ordered list of nodes."""

    # if the tree exists,
    if tree != None:
        # go to its left node, traverse that tree recursively
        traverse(tree["left"], sorted_array=sorted_array)
        if tree["root"] != None:
            # append the leftmost root of the current tree to list
            sorted_array.append(tree["root"])
        # then traverse the right node recursively
        traverse(tree["right"], sorted_array=sorted_array)

    # return populated list
    return sorted_array


## define sorting function
def treesort(array, tree=None):
    """Sorts an unordered list using the tree sort algorithm."""

    for i in array:
        # create a binary search tree by inserting each list element
        tree = insert(tree, i)

    # traverse the resulting tree from left to right to get a sorted list
    return traverse(tree)


# test
test_tree = treesort(input_arr)
print(test_tree)


#### Bubble Sort
### Reference:

## define helper functions
def listswap(list, index_1, index_2):

    temp_tuple = list[index_1], list[index_2]

    list[index_2], list[index_1] = temp_tuple

    return list


## define sorting algorithm
def bubblesort(original_list):
    # make a copy to prevent modifying in place; new list will be the new sorted list
    new_list = original_list.copy()
    # iterate over list as many times as there are elements
    for element in range(len(new_list)):
        # iterate over element-pairs (n-2, n-1)
        for list_index in range(len(new_list) - 1):
            if new_list[list_index] > new_list[list_index + 1]:
                # swap if condition met using helper function
                new_list = listswap(new_list, list_index, list_index + 1)

    return new_list


# test
test_bubble = bubblesort(input_arr)
print(test_bubble)


#### Plotting time complexity of each algorithm

# define x axis: number of elements with which to test each algorithm
x_axis = [i for i in range(0, 5000, 100)]


def get_sort_times(func, x):
    """For a pre-defined sorting algorithm, return a list of runtimes
    over a given list of lengths. """

    # instantiate empty list of times
    times = []

    # for each list length in the x axis
    for i in x:
        # make a list of that length, containing randomly sampled integers from 0 to 5000
        start_list = [randint(0, 5000) for i in range(5000)]
        # start the clock
        start_time = time.time()
        # call algorithm on the list
        func(start_list[:i])
        # calculate elapsed time
        elapsed_time = time.time() - start_time
        # add value to list of times
        times.append(elapsed_time)

    # return times
    return times


# get time runtime lists for each sorting algorithm
bubble_times = get_sort_times(bubblesort, x_axis)
tree_times = get_sort_times(treesort, x_axis)

# plot
plt.xlabel("No. of elements")
plt.ylabel("Time elapsed")
plt.plot(x_axis, bubble_times, label="Bubble Sort")
plt.plot(x_axis, tree_times, label="Tree Sort")
plt.grid(visible=True)
plt.legend()
plt.title("Bubble and Tree Sort Algorithm Time Complexity")
plt.savefig("hw4plot.pdf")
plt.show(block=False)
plt.close()
