from collections import deque
import heapq
import sys
input = sys.stdin.readline
V, E = map(int,input().split())
start = int(input())
array = [[] for _ in range(V+1)]
for _ in range(E):
    s,e,c = map(int,input().split())
    array[s].append([c,e])
cost = [999999999 for _ in range(V+1)]
cost[start] = 0
q = []
q.append((0,start))
while q:
    num, node = heapq.heappop(q)
    if cost[node] < num:
        continue
    for i in array[node]:
        if cost[node] + i[0] < cost[i[1]]:
            cost[i[1]] = cost[node] + i[0]
            heapq.heappush(q,(cost[i[1]],i[1]))
for i in range(1,V+1):
    if cost[i] == 999999999:
        print('INF')
    else:
        print(cost[i])
