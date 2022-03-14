import sys
from collections import deque, defaultdict


input = sys.stdin.readline

N = int(input())

space = []

fishes = defaultdict(int)

for i in range(N):
    a = list(map(int, input().split()))
    for j in a:
        fishes[j] += 1
    if 9 in a:
        s_l = [i, a.index(9)]
        a[int(a.index(9))] = 0
    space.append(a)

level = 2
eat = 0

queue = deque()

queue.append([s_l])

answer = 0

min_spot = []
min_path = 10000
max_path = 0

while queue:

    L = queue.popleft()

    x, y = L[-1]
    
    n, s, e, w = 0, 0, 0, 0
    if 0 <= x-1 < N:
        w = 1
    if 0 <= x+1 < N:
        e = 1
    if 0 <= y-1 < N:
        n = 1
    if 0 <= y+1 < N:
        s = 1
    
    if n == 1:
        if space[x][y-1] <= level:
            if 0 < space[x][y-1] < level and [x, y-1] not in L:
                min_spot.append([len(L), x, y-1])
                min_path = min(min_path, len(L))
                max_path = max(max_path, len(L))
            elif [x, y-1] not in L and (space[x][y-1] == level or space[x][y-1] == 0):
                queue.append(L + [[x, y-1]])

    if s == 1:
        if space[x][y+1] <= level:
            if 0 < space[x][y+1] < level and [x, y+1] not in L:
                min_spot.append([len(L), x, y+1])
                min_path = min(min_path, len(L))
                max_path = max(max_path, len(L))
            elif [x, y+1] not in L and (space[x][y+1] == level or space[x][y+1] == 0):
                queue.append(L + [[x, y+1]])

    if w == 1:
        if space[x-1][y] <= level:
            if 0 < space[x-1][y] < level and [x-1, y] not in L:
                min_spot.append([len(L), x-1, y])
                min_path = min(min_path, len(L))
                max_path = max(max_path, len(L))
            elif [x-1, y] not in L and (space[x-1][y] == level or space[x-1][y] == 0):
                queue.append(L + [[x-1, y]])

    if e == 1:
        if space[x+1][y] <= level:
            if 0 < space[x+1][y] < level and [x+1, y] not in L:
                min_spot.append([len(L), x+1, y])
                min_path = min(min_path, len(L))
                max_path = max(max_path, len(L))
            elif [x+1, y] not in L and (space[x+1][y] == level or space[x+1][y] == 0):
                queue.append(L + [[x+1, y]])

    if max_path != 0 and min_path != max_path:
        min_spot.sort()
        min_L, min_x, min_y = min_spot[0]
        answer += min_L
        queue = deque()
        queue.append([[min_x, min_y]])

        fishes[space[min_x][min_y]] -= 1



        eat += 1
        if level == eat:
            level += 1
            eat = 0
        
        space[min_x][min_y] = 0

        min_spot = []
        min_path = 10000
        max_path = 0

        token = 0

        for i in range(1, level):
            if fishes[i] > 0:
                token = 1
        if token == 0:
            break

    elif len(queue) == 0 and max_path != 0:
        min_spot.sort()
        min_L, min_x, min_y = min_spot[0]
        answer += min_L
        queue = deque()
        queue.append([[min_x, min_y]])

        fishes[space[min_x][min_y]] -= 1


        eat += 1
        if level == eat:
            level += 1
            eat = 0
        
        space[min_x][min_y] = 0

        min_spot = []
        min_path = 10000
        max_path = 0

        token = 0

        for i in range(1, level):
            if fishes[i] > 0:
                token = 1
        if token == 0:
            break

    elif len(queue) == 0 and max_path == 0:
        break 
print(answer)



