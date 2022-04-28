from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

def rotate(n):
    return list(map(list, zip(*n[::-1])))

table = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
shape = []
for i in range(5):
    temp = []
    for _ in range(4):
        temp.append(table[i])
        table[i] = rotate(table[i])
    shape.append(temp)
answer = 1000000000
flag = False
for nums in permutations(range(0, 5), 5):
    for a in range(4):
        if shape[nums[0]][a][0][0] == 0:
            continue
        if answer == 12:
            break

        for b in range(4):
            if answer == 12:
                break

            for c in range(4):
                if answer == 12:
                    break

                for d in range(4):
                    if answer == 12:
                        break

                    for e in range(4):
                        if answer == 12:
                            break
                        newtable = [shape[nums[0]][a], shape[nums[1]][b], shape[nums[2]][c], shape[nums[3]][d], shape[nums[4]][e]]
                        if newtable[0][0][0] == 1 and newtable[4][4][4] == 1:
                            q = deque([(0, 0, 0, 0)])
                            check = set([(0, 0, 0)])
                            dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
                            while q:
                                x, y, z, count = q.popleft()  
                                if (x, y, z) == (4, 4, 4):
                                    answer = min(answer, count)
                                    flag = True
                                    break
                                for i in range(6):
                                    ax = x + dx[i]
                                    ay = y + dy[i]
                                    az = z + dz[i]
                                    if 0 <= ax <= 4 and 0 <= ay <= 4 and 0 <= az <= 4 and newtable[ax][ay][az] == 1 and (ax, ay, az) not in check:
                                        q.append((ax, ay, az, count + 1))
                                        check.add((ax, ay, az))

if flag:
    print(answer)
else:
    print(-1)