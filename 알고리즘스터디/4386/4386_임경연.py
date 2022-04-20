from math import sqrt
import heapq

def calDist(a, b):
    x1, y1 = a
    x2, y2 = b
    return sqrt((x2-x1)**2 + (y2-y1)**2)

N = int(input())

nodes = []
nodes_length = [[] for _ in range(N)]
visited = [0] * N

for i in range(N):
    nodes.append(list(map(float, input().split())))

for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        else:
            dist = calDist(nodes[i], nodes[j])
            nodes_length[i].append([dist, j])
            nodes_length[j].append([dist, i])

heap = [[0, 1]]

answer = 0
cnt = 0

while heap:
    if cnt == N:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = 1
        answer += w
        cnt += 1
        for i in nodes_length[s]:
            heapq.heappush(heap, i)


print("{:.2f}".format(answer))
