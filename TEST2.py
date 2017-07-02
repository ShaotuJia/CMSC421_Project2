# This script is to test josn

import  json
import random

string = '[1, 2, 3, 4, "x", 5]'

print("type = ",type(string))

def digit_index(string:str):
    index = []
    for x in range(0,len(string)-1):
        if string[x].isdigit():
            index.append(x)

    return index

print("digit index = ", random.choice(digit_index(string)))






'''''''''
def f(x):
    return{1: "a", 2: "b",}[x]

x = 1

y = f(x)

print(y)



'''''''''
'''''''''
string = '["+", ["*", ["+", ["*", "x", 4], 2], ["+", "x", 1]], 3]'

List = ["+", ["*", ["+", ["*", "x", 4], 2], ["+", "x", 1]], 3]

List_string = str(List)

print("length of string", len(string))

J_string = json.loads(string)

print("length of List_string", len(List_string))

J_List_string = json.dumps(List)

'''