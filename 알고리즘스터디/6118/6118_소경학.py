from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
array = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)
visit = [0 for _ in range(n+1)]
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in array[x]:
        if visit[i] == 0:
            visit[i] = visit[x] + 1
            q.append(i)
t = max(visit[2:])
one = 0
two = t
three = 0
for i in range(2,n+1):
    if visit[i] == t:
        one = i
        break
for i in range(2,n+1):
    if visit[i] == t:
        three += 1
print(one,two,three)
