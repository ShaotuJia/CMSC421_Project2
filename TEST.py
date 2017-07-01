# This is to test possible functions

import json
import random

class Element:
    def __init__(self):
        self.e = None
        self.parent = None
        self.child = None


fx = '["+", ["*", ["+", "x", 2], ["+", "x", 1]], 3]'

fx = json.dumps(fx)


# return the index of '[' and ']'
def where_bracket(aList, Number):

    if Number >= aList.count('['):
        print('Beyond the range of [')
        return 1

    left_counter = 0
    right_counter = 0
    index = []
    for left_index in range(0, len(aList)-1):
        if aList[left_index] == '[':
            left_counter += 1
        if left_counter == Number:
            index.append(left_index)
            break

    for right_index in range(len(aList)-1, 0):
        if aList[right_index] == ']':
            right_counter += 1
        if right_counter == Number:
            index.append(right_index)
            break

    return index

index = where_bracket(fx, 1)
print('the location of bracket', index)













'''''''''''
fx = json.loads(fx)

openSet = []
closeSet = []

openSet = openSet + fx

while not (not openSet):
    for x in openSet:




first_tree = []
second_tree = []
third_tree = []
fx_copy = [first_tree, second_tree, third_tree]
first_tree = fx[0]
second_tree = fx[1]
third_tree = fx[2]

second_tree = fx[1][2]

#This functions is to find how many levels in the tree
def levels(tree):
    for i in range(1,2):
        for j in range(0,2):
            tree[i] += tree[i][j]


def select_subtree(tree, level):
    for

'''