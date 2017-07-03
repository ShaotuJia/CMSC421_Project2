#!/usr/bin/env python3

# This script is to find the best equation for given data using genetic algorithm

# Fitness function: The sum of squared error
# Step 1: Randomly Generate 100 equations as total population using initial() function
# Step 2: Pick two equations that has best heuristic value
# Step 3: Make a new element using picked two equations by crossover and the new element has 10% to mutate
# Step 4: Append the new element to total population and remove one old generation element
# Step 5: Repeat step 2 to step 4 by 10 times to get 10 generations
# Step 6: Print the equation after 10 generations

# !! More accurate result can be obtained by increasing the 'size of population' and 'number of generation'!

import json
import random
import math


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


def initial():
    # It is better to have non-uniform random to make the initial() hard to create large size tree !
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


# Select subtree from original tree
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


# Define crossover function
# !!! This crossover function has been changed and is different to the function in 'crossover' file
def crossover(arg_first: str, arg_second: str):

    lucky_No_1 = random.randint(1, arg_first.count("["))

    lucky_No_2 = random.randint(1, arg_second.count("["))

    which_bracket_first = left_bracket(arg_first, lucky_No_1)
    which_bracket_second = left_bracket(arg_second, lucky_No_2)

    subtree_first = select_subtree(arg_first, which_bracket_first)
    subtree_second = select_subtree(arg_second, which_bracket_second)

    child = arg_first.replace(subtree_first,subtree_second)

    return child


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


def equation_value(eq: str, x: int):      # Find the value of equation

    result = ""

    while eq.count("[") != 0:
        unit = min_unit(eq)
        element_No_unit = len(json.loads(unit))

        if element_No_unit == 2:
            result = str(unary_operation(unit, x))
        if element_No_unit == 3:
            result = str(binary_operation(unit,x))
        eq = eq.replace(unit, result)

    value = float(eq)
    return value


def sum_error(data:list, function:str):
    error_list = []
    for i in range(0,len(data)):
        eq_result = equation_value(function, i)
        error = data[i] - eq_result
        error_list.append(math.pow(error, 2))

    return sum(error_list)


# Initialize the total population
def initial_population(amount: int):
    total = []
    for i in range(0, amount):
        total.append(initial())
    return total


# Find the element with smallest error in population
def heurstic(data:list, population: list):
    error = float("inf")
    best_eq = ""
    for i in population:
        temp_error = sum_error(data, i)
        if temp_error < error:
            error = temp_error
            best_eq = i

    return best_eq


# Find parents which are the two equations with smallest error
def find_parents(data:list, total_pop:list):
    parents = []
    total = []
    total.extend(total_pop)
    first_parent = heurstic(data, total)
    parents.append(first_parent)
    total.remove(parents[0])
    second_parent = heurstic(data, total)
    parents.append(second_parent)
    return parents


def optimize(data: list, population_size: int, generation: int):
    group = initial_population(population_size)
    for i in range(0, generation):
        parents = find_parents(data, group)
        child = crossover(parents[0], parents[1])
        first_size = len(group)
        group.pop(0)
        before_size = len(group)
        group.append(child)
        after_size = len(group)

    return heurstic(data, group)


################################################################################################
population_size = 5
generation = 5

population = initial_population(population_size)
data = []

with open('data/oscillator.json') as data_file:
    data = json.load(data_file)



best_equation = optimize(data, population_size, generation)
error = sum_error(data, best_equation)
print("The best equation: ", best_equation)
print("The sum of square error: ", error)










