from re import M
import sys
from collections import deque
input = sys.stdin.readline

N, e, w, s, n = map(int, input().split())

prob = [e/100, w/100, s/100, n/100]

start = (14, 14)

def east(a):
    i = a[0] + 1
    j = a[1]
    return (i, j)
def west(a):
    i = a[0] - 1
    j = a[1]
    return (i, j)
def south(a):
    i = a[0]
    j = a[1] + 1
    return (i, j)
def north(a):
    i = a[0]
    j = a[1] - 1
    return (i, j)


queue = deque()
queue.append([1, start])

answer = 0

while queue:
    a = queue.pop()
    if len(a) == N + 2:
        answer += a[0]
        continue
    else:
        b = a[-1]
        for i, j in enumerate(prob):
            if j == 0:
                continue
            else:
                if i == 0:
                    c = east(b)
                    if c not in a:
                        queue.append([a[0] * prob[0]] + a[1:] + [c])
                if i == 1:
                    c = west(b)
                    if c not in a:
                        queue.append([a[0] * prob[1]] + a[1:] + [c])
                if i == 2:
                    c = south(b)
                    if c not in a:
                        queue.append([a[0] * prob[2]] + a[1:] + [c])
                if i == 3:
                    c = north(b)
                    if c not in a:
                        queue.append([a[0] * prob[3]] + a[1:] + [c])

print(answer)






