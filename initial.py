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
#tree = [binary_operator(), 'x', real_rand()]

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



'''
def convert_dic(f_x):
    for i in range(0, len(f_x) - 1):
        if f_x[i] == "[":
            f_x[i] = "{"

        if f_x[i] == "]":
            f_x[i] = "]}"

        if f_x[i] == "+" or "-" or "*":
            f_x[i] = ":["

    return f_x


fx = convert_dic(fx)

print(fx)

'''
'''
dict_ = {1: 2, 3: 4, "55": "66"}

# test json.dumps

print (type(dict_), dict_)
json_str = json.dumps(dict_)
print ("json.dumps(dict) return:")
print (type(json_str), json_str)

# test json.loads
print("\njson.loads(str) return")
dict_2 = json.loads(json_str)
print(type(dict_2), dict_2)
'''
