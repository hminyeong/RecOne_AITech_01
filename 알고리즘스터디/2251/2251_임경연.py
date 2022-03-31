import sys
from collections import deque
import copy

input = sys.stdin.readline

A, B, C = map(int, input().split())

limit = (A, B, C)
direction = {0:(0, 1), 1:(0, 2), 2:(1, 0), 3:(1, 2), 4:(2, 0), 5:(2, 1)}

answer = []

q = deque()
status = [[0, 0, C]]
q.append([0, 0, C])

while q:
    s = q.popleft()

    for i in range(6):
        tmp_s = copy.deepcopy(s)
        x, y = direction[i]
        
        if s[x] == 0:
            continue

        else:
            move = min(s[x], limit[y] - s[y])
            tmp_s[x] = tmp_s[x] - move
            tmp_s[y] = tmp_s[y] + move

            if tmp_s in status:
                continue
            else:
                q.append(tmp_s)
                status.append(tmp_s)

answer = []

for i in status:
    if i[0] == 0:
        answer.append(i[2])

answer = list(set(answer))

answer.sort()

answer = list(map(str, answer))

print(" ".join(answer))

            
        