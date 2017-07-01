# This script is to replace some subtree of the JSON-expression with a new, random subtree.
# Like with initial, repeatedly running mutate should produce varying random 'mutations'

import json
import random
f = json.dumps(["+", ["*", 2, ["+", "x", 1]], 3])

fx = '["+", "x", 1]'

print("fx = ", type(fx))

fx = json.loads(fx)


# randomly generate binary operator
def binary_operator() -> object:
    b_list = ["+", "-", "*"]
    b_index = random.randint(0,2)
    return b_list[b_index]


# Randomly generate unary operator
def unary_operator():
    u_list = ["e", "sin", "cos"]
    u_index = random.randint(0,2)
    return u_list[u_index]


def real_rand():
    return random.uniform(-100, 100)


def rand_element():
    index = random.randint(0,1)
    if index == 0:
        return [binary_operator(), 'x', real_rand()]
    else:
        return real_rand()
