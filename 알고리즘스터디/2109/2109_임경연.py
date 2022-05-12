import heapq

N = int(input())

lectures = []

D = 0
for i in range(N):
    p, d = map(int, input().split())
    D = max(D, d)
    heapq.heappush(lectures, [-p, d])

plan = [0] * (D+1)
plan[0] = 1

answer = 0
while lectures and 0 in plan:
    p, d = heapq.heappop(lectures)
    if plan[d] == 0:
        plan[d] = 1
        answer += p
    else:
        while d != 0:
            if plan[d] == 0:
                plan[d] = 1
                answer += p
                break
            d -= 1
print(-answer)
    
