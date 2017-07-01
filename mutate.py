# This script is to replace some subtree of the JSON-expression with a new, random subtree.
# Like with initial, repeatedly running mutate should produce varying random 'mutations'

import json
import random


fx = '["+", ["*", ["+", ["*", "x", 4], 2], ["+", "x", 1]], 3]'


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

tree_height = random.randint(2,5)
tree = []
tree = binary_operator()
tree = [binary_operator(), 'x', real_rand()]

for level in range(2, tree_height):
    lucky_index = random.randint(0,2)
    if lucky_index == 0:
        tree = [binary_operator(), tree, rand_element()]
    elif lucky_index == 1:
        tree = [binary_operator(), rand_element(), tree]
    else:
        tree = [binary_operator(), tree,tree]


#tree is a random generated function
print("the random tree is ", tree)
print("the type of tree is", type(tree))


# This function is to find the index of left bracket. Number = 3 mean the third left bracket
def left_bracket(aList, Number):

    if Number >= aList.count('['):
        print('Beyond the range of [')
        return 1

    left_counter = 0

    for left_index in range(0, len(aList)-1):
        if aList[left_index] == '[':
            left_counter += 1
        if left_counter == Number:
            return left_index


def select_subtree(tree, left_index):
    truth = False
    subtree = tree[left_index]
    left_index = left_index + 1
    while truth is False:
        element= tree[left_index]
        subtree = subtree + element
        try:                            # Apply the property of JSON experssion
            json.loads(subtree)
            truth = True
        except:
            left_index += 1

    return subtree

tree = json.dumps(tree)
left_index = left_bracket(tree,2)
subtree = select_subtree(tree, left_index)
print("the seperated subtree is ", subtree)
print("the type of subtree is ", type(subtree))


#This function is to replace a part of original tree by new random tree
def mutate (original_tree:str, random_tree:str):
    total_level = original_tree.count("[")
    subtree_level = random.randint(2,total_level)
    bracket_left = left_bracket(original_tree, subtree_level)

    replace_subtree = select_subtree(original_tree, bracket_left)
    new_tree = original_tree.replace(replace_subtree,random_tree)
    return new_tree

new_tree = mutate(fx, tree)

print("the new tree is", new_tree)


