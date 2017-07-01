# This script is to test josn

import  json

string = '["+", ["*", ["+", ["*", "x", 4], 2], ["+", "x", 1]], 3]'

List = ["+", ["*", ["+", ["*", "x", 4], 2], ["+", "x", 1]], 3]

List_string = str(List)

print("length of string", len(string))

J_string = json.loads(string)

print("length of List_string", len(List_string))

J_List_string = json.dumps(List)