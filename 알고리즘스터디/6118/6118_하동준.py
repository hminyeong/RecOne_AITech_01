from collections import deque
import sys
input = sys.stdin.readline
MIN = -int(1e9)
MAX = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 양방향 그래프 생성 노드와 노드에 이어딘 엣지
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
    # 큐 초기화하고 시작노드 큐인

    while q:
        
        now, dist = q.popleft()
        visited[now] = True
        # 현재노드팝 후 현재

        if dist_ans < dist:
            min_ans = now
            dist_ans = dist
            count_ans = 1
        # 거리갱신

        elif dist_ans == dist:
            min_ans = min(min_ans, now)
            count_ans += 1
        # 거리 같으면

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist+1))
        # 팝한 노드에 연결된 노드를 큐에 넣는다
        
bfs(1, 0)
print(min_ans, dist_ans, count_ans)