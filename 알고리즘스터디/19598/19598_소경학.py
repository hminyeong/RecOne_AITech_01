import heapq
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
array.sort()
idx = 0
check = []
t = 0
answer = 0
while True:
    while True:
        if t == array[idx][0]:
            heapq.heappush(check,array[idx][1])
            idx += 1
            answer = max(answer,len(check))
        else:
            break
        if idx >= n:
            break
    if idx >= n:
        break
    t += 1
    while check:
        if check[0] == t:
            heapq.heappop(check)
        else:
            break
print(answer)
