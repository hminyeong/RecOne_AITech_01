from itertools import permutations
import sys
input = sys.stdin.readline
a, b = input().split()
a = list(a)
array = permutations(a,len(a))

mx = -1
for i in array:
    if i[0] == '0':
        continue
    else:
        if int("".join(i)) < int(b):
            mx = max(mx,int("".join(i)))
print(mx)