import heapq as hq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = []

for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))

a.sort(key = lambda x: x[0])
cnt = 1

b = [0]

for start ,end in a:
    if start >= b[0]:
        hq.heappop(b)
    else:
        cnt+=1
    hq.heappush(b, end)

print(cnt)