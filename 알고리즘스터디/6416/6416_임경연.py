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

tree_ = defaultdict(list)
for tree in trees:
    l = trees[tree]
    token = 0
    parent = []
    child = []
    if len(l) == 2:
        print(f"Case {tree} is a tree.")
        continue
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
        tree_[x].append(y)
        if x not in parent:
            parent.append(x)
    root = 0
    for p in parent:
        if p not in child:
            root += 1
    if root != 1:
        token = 1
    if token == 1:
        print(f"Case {tree} is not a tree.")            
    else:
        print(f"Case {tree} is a tree.")
