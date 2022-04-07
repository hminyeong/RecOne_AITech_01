import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())

space = [[] for _ in range(N)]

for i in range(M):
    x, y, d = map(int, input().split())
    space[x-1].append((y-1, d))


INF = int(1e10)
def dijkstra(start):
    distance = [INF] * N
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in space[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance

answer = []

for i in range(N):
    d = dijkstra(i)
    answer.append(d[X-1])

d_ = dijkstra(X-1)

for i in range(N):
    answer[i] += d_[i]

print(max(answer))





