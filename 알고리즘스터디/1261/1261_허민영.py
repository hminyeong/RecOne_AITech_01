import sys
import heapq

input = sys.stdin.readline

#기본 정보
m,n = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

INF = int(1e9)
distance = [[INF]*m for _ in range(n)]
graph = [list(map(int, input().strip())) for _ in range(n)] #strip() !!!!!!!!

#함수 정의
def dijkstra():
    q = []
    heapq.heappush(q, (0,0,0))
    distance[0][0] = 0
    while q:
        cost,x ,y = heapq.heappop(q)
        if x == n-1 and y == m-1:
            return print(distance[n-1][m-1])
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < m:
                new_cost = cost + graph[new_x][new_y]
                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q,(new_cost, new_x, new_y))

dijkstra()
