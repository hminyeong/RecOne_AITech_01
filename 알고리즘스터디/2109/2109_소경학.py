import heapq
n = int(input())
array = [[] for _ in range(10001)]
for _ in range(n):
    p, d = map(int,input().split())
    array[d].append(p)
cnt = []
total = 0
for i in range(10000,0,-1):
    if len(array[i]) > 0:
        for j in array[i]:
            heapq.heappush(cnt,-j)
    if len(cnt) > 0:
        total += heapq.heappop(cnt)

print(-total)