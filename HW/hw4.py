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

input_arr = [3, 4, 5, 6, 2, 1]

# tree sort

# helper functions
def insert(tree, k):

    if tree == None:
        tree = {"root": k, "left": None, "right": None}
        return tree

    if k < tree["root"]:
        tree["left"] = insert(tree["left"], k)

    elif k > tree["root"]:
        tree["right"] = insert(tree["right"], k)

    return tree


def traverse(tree, sorted_array=[]):
    if tree != None:
        traverse(tree["left"], sorted_array=sorted_array)
        if tree["root"] != None:
            sorted_array.append(tree["root"])
        traverse(tree["right"], sorted_array=sorted_array)
    return sorted_array


# sorting algorithm
def treesort(array, tree=None):

    for i in array:
        tree = insert(tree, i)

    return traverse(tree)


# test
test_tree = treesort(input_arr)
print(test_tree)


# bubble sort

# helper functions
def listswap(list, index_1, index_2):

    temp_tuple = list[index_1], list[index_2]

    list[index_2], list[index_1] = temp_tuple

    return list


# sorting algorithm
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


# get time complexity of each algorithm

x_axis = [i for i in range(0, 10000, 100)]


def get_sort_times(func, x):
    times = []
    for i in x:
        start_list = [randint(0, 5000) for i in range(10000)]
        start_time = time.time()
        func(start_list[:i])
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)
    return times


bubble_times = get_sort_times(bubblesort, x_axis)
tree_times = get_sort_times(treesort, x_axis)


bubble_times = []

for i in x_axis:
    start_list = [randint(0, 5000) for i in range(10000)]
    start_time = time.time()
    sorted_list = bubblesort(start_list[:i])
    elapsed_time = time.time() - start_time
    bubble_times.append(elapsed_time)


tree_times = []

for i in x_axis:
    start_list = [randint(0, 5000) for i in range(10000)]
    start_time = time.time()
    sorted_list = treesort(start_list[:i])
    elapsed_time = time.time() - start_time
    tree_times.append(elapsed_time)


plt.xlabel("No. of elements")
plt.ylabel("Time elapsed")
plt.plot(x_axis, bubble_times, label="Bubble Sort")
plt.plot(x_axis, tree_times, label="Tree Sort")
plt.grid(visible=True)
plt.legend()
plt.show()
