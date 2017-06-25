# This program is for project 2

import json
import matplotlib.pyplot as plt

f = json.dumps(["+", ["*", 2, ["+", "x", 1]], 3])

fx = {"+": [{"*":[2, {"+":["x",1]}]}, 3]}

fx = json.dumps(fx)

print(fx)


