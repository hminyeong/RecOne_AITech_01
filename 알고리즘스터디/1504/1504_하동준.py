import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# n,m = map(int,input().split())
# start = int(input())

# graph = [[]for _ in range(n+1)]
# distance = [INF]*(n+1)

# for _ in range(m):
#     a,b,c=map(int,input().split())
#     graph[a].append(b,c)

# def dijkstra(start):
#     q = []

#     heapq.heappush(q,(0,start))
#     distance[start] = 0

#     while q:
#         dist,now = heapq.heappop(q)

#         if distance[now] < dist:
#             continue
        
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(start)

# for i in range(1,n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

# todo 1 to N 
N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

v1,v2= map(int, input().split())

# start = 1

# print(N,E,v1,v2)

# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3



def dijkstra(start):
    dp = [INF for i in range(N + 1)]

    q=[]
    heapq.heappush(q,(0,start))
    dp[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if(dp[now] < dist):
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < dp[i[0]]:
                dp[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return dp

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])
print(cnt if cnt < INF else -1)




