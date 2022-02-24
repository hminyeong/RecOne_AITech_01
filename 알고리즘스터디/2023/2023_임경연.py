import sys
import math
from collections import deque

input = sys.stdin.readline

N = int(input())

a = ['2', '3', '5', '7']
a = deque(a)
b = ['1', '3', '5', '7', '9']


while True:
    if len(a[0]) == N:
        break

    n = a.popleft()

    for i in b:
        m = str(n) + str(i)
        for j in range(2, int(math.sqrt(int(m))) + 1):
            if int(m) % j == 0:
                break
            elif j == int(math.sqrt(int(m))):
                a.append(str(m))
                

for i in a:
    print(i)