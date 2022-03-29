import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

maps = [[] for _ in range(N)]

def issquare(n):
    if n == "":
        return False
    else:
        return int(int(n) ** 0.5) ** 2 == int(n)

for i in range(N):
    inputs = input()
    for j in range(M):
        maps[i].append(inputs[j])

answer = -1

for i in range(M):
    for j in range(N):
        for a in range(2*M+1):
            for b in range(2*N+1):
                move_x = M - a
                move_y = N - b

                x = copy.deepcopy(i)
                y = copy.deepcopy(j)
                
                number = ""
                while (0 <= x <= M - 1) and (0 <= y <= N - 1):
                    
                    number += maps[y][x]
                    if issquare(number):
                        answer = max(answer, int(number))
                    if move_x == 0 and move_y == 0:
                        break
                    x = x + move_x
                    y = y + move_y
                
                

print(answer)



