import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

space = []


for i in range(M):
    space.append(list(input())[:N])

dist = [[-1] * N for _ in range(M)] 
dist[0][0] = 0

r, l, u, d = (1, 0), (-1, 0), (0, -1), (0, 1)

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()

    for i in [r, l, u, d]:
        x_, y_ = i

        nx = x + x_
        ny = y + y_

        if 0 <= nx < N and 0 <= ny < M:
            if dist[ny][nx] == -1:
                if space[ny][nx] == "0":
                    queue.appendleft((nx, ny))
                    dist[ny][nx] = dist[y][x]
                elif space[ny][nx] == "1":
                    queue.append((nx, ny))
                    dist[ny][nx] = dist[y][x] + 1

print(dist[M-1][N-1])