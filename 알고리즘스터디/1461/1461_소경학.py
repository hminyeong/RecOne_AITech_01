from itertools import permutations
n, m = map(int,input().split())
array = list(map(int,input().split()))
plus = []
minus = []
for i in array:
    if i < 0:
        minus.append(i)
    elif i > 0:
        plus.append(i)
mn = 99999999999999
minus.sort()
plus.sort(reverse=True)
cnt = 0
for i in range(0,len(plus),m):
    cnt += 2*plus[i]
for i in range(0,len(minus),m):
    cnt += 2*abs(minus[i])
for i in array:
    cnt2 = cnt - abs(i)
    mn = min(mn,cnt2)
print(mn)