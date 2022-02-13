import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
array = []
for _ in range(m):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x:x[2])

check = [i for i in range(n+1)]
def find(x):
    if check[x] == x:
        return x
    check[x] = find(check[x])
    return check[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x<y:
        check[x] = y
    else:
        check[y] = x

cnt = 0
for i in array:
    if find(i[0]) != find(i[1]):
        union(i[0],i[1])
        cnt += i[2]
print(cnt)