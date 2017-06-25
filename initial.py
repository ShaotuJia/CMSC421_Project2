# This Script is the randomly generate a function in JSON experssion

import json
import random


# randomly generate binary operator
def binary_operator() -> object:
    b_list = ["+", "-", "*"]
    return random.sample(b_list, 1)


# Randomly generate unary operator
def unary_operator():
    u_list = ["e", "sin", "cos"]
    return random.sample(u_list, 1)


def real_rand():
    return random.uniform(-100, 100)


def rand_leaf():
    possible_node = [binary_operator(), real_rand()]
    return [random.sample(possible_node, 1), random.sample(possible_node, 1)]


tree_height = random.randint(1, 7)  # this is the height of tree

tree = []
leaf = []
for layer_No in range(1, tree_height):


    leaf = []
    # tree = {binary_operator(): leaf}

    if layer_No == tree_height:
        leaf = ["x", real_rand()]
    else:
        leaf = rand_leaf()

    operator = binary_operator()
    tree = {operator: leaf}

    for node in leaf:
        if node == "+" or "-" or "*":
            sub_tree = tree[node]
            tree[node] = {tree:rand_leaf()}