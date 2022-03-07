import sys
import heapq

input = sys.stdin.readline

#기본 정보
n,m = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra():
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra()

#출력
maxi_distance = max(distance[1:])
#index()는 리스트 중에서 특정한 원소가 몇 번째에 처음으로 등장했는지를 알려줌
print(distance.index(maxi_distance), maxi_distance, distance.count(maxi_distance))
