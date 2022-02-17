import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())

l = defaultdict(list)
for num in range(1, N + 1):
    l[num] = [[], []]

for _ in range(M):
    x, y = map(int, input().split())
    l[x][1].append(y)
    l[y][0].append(x)

answer = []

for _ in range(1, N + 1):
    up_visited = [0] * (N+1)
    down_visited = [0] * (N+1)
    up_stack = [_]
    down_stack = [_]
    up_answer = []
    down_answer = []
    while up_stack:
        tmp = up_stack.pop()
        
        for i in l[tmp][0]:
            if up_visited[i] == 0:
                up_visited[i] = 1
                up_answer.append(i)
                up_stack.append(i)
                
    while down_stack:
        tmp = down_stack.pop()
        
        for i in l[tmp][1]:
            if down_visited[i] == 0:
                down_visited[i] = 1
                down_stack.append(i)
                down_answer.append(i)
    
    answer.append(up_answer + down_answer)

for i in answer:
    print(N - len(i) - 1)