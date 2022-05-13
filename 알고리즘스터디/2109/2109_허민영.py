import sys
import heapq

input = sys.stdin.readline

answer = []
n = int(input())
m_list = []
for _ in range(n):
    p, d = map(int, input().split())
    m_list.append((p, d))

m_list.sort(key=lambda x:(x[1], -x[0]))
day = 1

for i in range(n):
    if m_list[i][1] >= day:
        day += 1
        heapq.heappush(answer, m_list[i][0])
    else:
        if m_list[i][0] > answer[0]:
            heapq.heappop(answer)
            heapq.heappush(answer, m_list[i][0])

print(sum(answer))