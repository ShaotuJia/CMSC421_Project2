#!/usr/bin/env python3


import json
import random
import time

random.seed(time.time())  # The random seed is the current system time


# randomly generate binary operation
def binary_operator() -> object:
    b_list = ["+", "-", "*"]
    b_index = random.randint(0,2)
    return b_list[b_index]


# randomly generate unary operation
def variable_rand():
    rand_index = random.randint(0,3)
    return {0: ["e", "x"], 1: ["sin", "x"], 2: ["cos","x"], 3: "x"}[rand_index]


# Generate random real number from -1000 to 1000
def real_rand():
    return float("{0:.2f}".format(random.uniform(-1000, 1000)))


# Randomly choose a minimum expression or a real number
def rand_element():
    index = random.randint(0,1)
    if index == 0:
        return [binary_operator(), variable_rand(), real_rand()]
    else:
        return real_rand()


# Generate random expression with uniform tree height
def initial():
    tree_height = random.randint(2,5)
    tree = [binary_operator(), variable_rand(), real_rand()]

    for level in range(2, tree_height):
        lucky_index = random.randint(0,2)
        if lucky_index == 0:
            tree = [binary_operator(), tree, rand_element()]
        elif lucky_index == 1:
            tree = [binary_operator(), rand_element(), tree]
        else:
            tree = [binary_operator(), tree,tree]
    return json.dumps(tree)


print(initial())
