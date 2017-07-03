#!/usr/bin/env python3

# This script is to randomly swap the subtree of two JOSN expression

import json
import random
import sys

try:
    arg_1 = sys.argv[1]
    arg_2 = sys.argv[2]
except:
    print("The format of Equation Expression is Wrong !!")


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


def crossover(arg_first:str, arg_second:str):

    lucky_No_1 = random.randint(1, arg_first.count("["))
    lucky_No_2 = random.randint(1, arg_second.count("["))

    which_bracket_first = left_bracket(arg_first, lucky_No_1)
    which_bracket_second = left_bracket(arg_second, lucky_No_2)

    subtree_first = select_subtree(arg_first, which_bracket_first)
    subtree_second = select_subtree(arg_second, which_bracket_second)

    new_first = arg_first.replace(subtree_first,subtree_second)
    new_second = arg_second.replace(subtree_second,subtree_first)

    new_first = json.loads(new_first)
    new_second = json.loads(new_second)

    print(new_first)
    print(new_second)


crossover(arg_1,arg_2)



