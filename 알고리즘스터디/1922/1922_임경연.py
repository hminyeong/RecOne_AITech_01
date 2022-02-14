import sys
import heapq

input = sys.stdin.readline

A = int(input())
B = int(input())

visited = [0] * (A + 1)

lines = [[] for _ in range(A+1)]
heap = [[0, 1]]

for _ in range(B):
    a, b, c = map(int, input().split())
    lines[a].append([c, b])
    lines[b].append([c, a])


answer = 0

cnt = 0

while heap:
    if cnt == A:
        break

    print(heap)

    a, b = heapq.heappop(heap)
    if visited[b] != 1:
        visited[b] = 1
        answer += a
        cnt += 1
        
        for i in lines[b]:
            heapq.heappush(heap, i)

print(answer)
