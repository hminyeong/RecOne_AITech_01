import heapq

N = int(input())

conf = []

for i in range(N):
    heapq.heappush(conf, list(map(int, input().split())))

rooms = []

for i in range(N):
    s, e = heapq.heappop(conf)
    if not rooms:
        heapq.heappush(rooms, e)
    else:
        shortest_end = heapq.heappop(rooms)
        heapq.heappush(rooms, e)
        if s < shortest_end:
            heapq.heappush(rooms, shortest_end)
        else:
            continue

print(len(rooms))