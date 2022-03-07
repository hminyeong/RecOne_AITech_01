from collections import deque
import sys
input = sys.stdin.readline
MIN = -int(1e9)
MAX = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist_ans = MIN
min_ans = MAX
count_ans = 0

def bfs(start, d):
    global dist_ans, count_ans, min_ans
    q = deque()
    q.append((start, d))
    while q:
        now, dist = q.popleft()
        visited[now] = True
        if dist_ans < dist:
            min_ans = now
            dist_ans = dist
            count_ans = 1
        elif dist_ans == dist:
            min_ans = min(min_ans, now)
            count_ans += 1
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist+1))
bfs(1, 0)
print(min_ans, dist_ans, count_ans)