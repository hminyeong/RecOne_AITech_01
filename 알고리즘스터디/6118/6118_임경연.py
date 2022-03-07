import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

routes = [[] for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    routes[x-1].append(y-1)
    routes[y-1].append(x-1)

visited = [0] * N

queue = deque()

queue.append(0)
visited[0] = 1

while queue:
    node = queue.popleft()

    for i in routes[node]:
        if visited[i] == 0:
            visited[i] = visited[node] + 1
            queue.append(i)


a = max(visited)
b = visited.index(a) + 1
c = visited.count(a)

print(b, a - 1, c)

