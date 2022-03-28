import sys
from collections import defaultdict

input = sys.stdin.readline

trees = defaultdict(list)

inputs = []
num_tree = 1

while True:
    input_ = input().split()
    if "-1" in input_:
        break
    if "0" in input_:
        inputs = inputs + input_
        trees[num_tree] = inputs
        inputs = []
        num_tree += 1
        continue
    inputs = inputs + input_


for tree in trees:
    l = trees[tree]
    token = 0
    parent = []
    child = []
    root = "None"
    while True:
        x = l.pop(0)
        y = l.pop(0)
        if x == "0":
            break
        if y not in child:
            child.append(y)
        else:
            token = 1
            break
        if root == "None" and x not in parent:
            parent.append(x)
        elif root == "None":
            parent.append(x)
            root = x
        elif root != x:
            print(tree, x, y)
            token = 1
            break
    if token == 0:
        print(f"Case {tree} is a tree.")
    else:
        print(f"Case {tree} is not a tree.")