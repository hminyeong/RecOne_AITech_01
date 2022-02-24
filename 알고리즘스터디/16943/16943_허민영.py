from itertools import permutations
import sys
input = sys.stdin.readline

a, b = input().split()
b = int(b)

c = -1
a_list = []
for i in permutations(a):
    a_list.append(''.join(i))

#print(a_list)
for i in a_list:
    if i[0] == '0':  # 0으로 시작
        continue
    
    i = int(i)
    if i < b:
        c = max(c, i)

print(c)
