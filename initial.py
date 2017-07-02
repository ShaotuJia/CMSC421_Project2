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


def variable_rand():
    rand_index = random.randint(0,3)
    return {0:["e", "x"], 1: ["sin", "x"], 2: ["cos","x"], 3: "x"}[rand_index]


def real_rand():
    return float("{0:.2f}".format(random.uniform(-1000, 1000)))


def rand_element():
    index = random.randint(0,1)
    if index == 0:
        #return [binary_operator(), 'x', real_rand()]
        return [binary_operator(), variable_rand(), real_rand()]
    else:
        return real_rand()


tree_height = 3
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

# Directly convert list to string cannot be used in json.loads !!!

def convert_string(list):
    string = str(list)
    j_string = ""
    for x in string:
        if x == "\\":
            continue
        else:
            j_string = j_string + x
    return j_string



tree = json.dumps(tree)

print(tree)
