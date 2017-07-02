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


def variable_rand():
    rand_index = random.randint(0,3)
    return {0:["e", "x"], 1: ["sin", "x"], 2: ["cos","x"], 3: "x"}[rand_index]


def real_rand():
    return float("{0:.2f}".format(random.uniform(-1000, 1000)))


def rand_element():
    index = random.randint(0,1)
    if index == 0:
        return [binary_operator(), variable_rand(), real_rand()]
    else:
        return real_rand()


def digit_index(string:str):
    index = []
    for x in range(0,len(string)-1):
        if string[x].isdigit():
            index.append(x)

    return index


tree_height = random.randint(2,5)
tree = []
tree = binary_operator()
tree = [binary_operator(), variable_rand(), real_rand()]

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

    if Number > aList.count('['):
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
which_bracket = random.randint(1, tree.count("["))
left_index = left_bracket(tree,which_bracket)
subtree = select_subtree(tree, left_index)
print("the seperated subtree is ", subtree)
print("the type of subtree is ", type(subtree))


#This function is to replace a part of original tree by new random tree
def mutate (original_tree:str, random_tree:str):

    lucky_number = random.randint(0, 1)

    if lucky_number == 0:
        digit_index_list = digit_index(original_tree)
        replace_digit_index = random.choice(digit_index_list)
        new_tree = original_tree.replace(original_tree[replace_digit_index],random_tree)
    else:
        total_level = original_tree.count("[")
        subtree_level = random.randint(2, total_level)
        bracket_left = left_bracket(original_tree, subtree_level)

        replace_subtree = select_subtree(original_tree, bracket_left)
        new_tree = original_tree.replace(replace_subtree,random_tree)
    return new_tree

new_tree = mutate(fx, tree)

print("the new tree is", new_tree)
