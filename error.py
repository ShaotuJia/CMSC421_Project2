#!/usr/bin/env python3

# This script is to calculate the sum of squared error for a given JOSN-expression and data file

import json
import math
import sys


file = sys.argv[1]

try:
    json.loads(sys.argv[2])
    fx = sys.argv[2]
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


def min_unit(string:str):
    bracket_amount = string.count("[")
    for order in range(1, bracket_amount + 1):
        left_index = left_bracket(string, order)
        subtree = select_subtree(string, left_index)
        if subtree.count("[") == 1:
            return subtree     # return a string


def unary_operation(unit:str, x:int):   # Find the value of unary operation
    return {'["e", "x"]': math.exp(x), '["sin", "x"]':math.sin(x), '["cos", "x"]':math.cos(x)}[unit]


def binary_operation(unit:str, x:int):  # Find the value of binary operation
    unit = json.loads(unit)

    for i in range(0, len(unit)):                      #replace x by its value
        if unit[i] == "x":
            unit[i] = x
    return {"+": unit[1] + unit[2], "-":unit[1] - unit[2], "*":unit[1]*unit[2]}[unit[0]]


def equation_value(eq:str, x:int):      # Find the value of equation

    result = ""

    while eq.count("[") != 0:
        unit = min_unit(eq)
        element_No_unit = len(json.loads(unit))

        if element_No_unit == 2:
            result = str(unary_operation(unit, x))
        if element_No_unit == 3:
            result = str(binary_operation(unit,x))
        eq = eq.replace(unit, result)

    return float(eq)


def sum_error(data:list, function:str):
    error_list = []
    for i in range(0,len(data)):
        eq_result = equation_value(function, i)
        error = data[i] - eq_result
        error_list.append(math.pow(error, 2))

    return sum(error_list)

data = []

with open(file) as data_file:
    data = json.load(data_file)


print(sum_error(data, fx))






