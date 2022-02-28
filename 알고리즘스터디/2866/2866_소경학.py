import sys
input = sys.stdin.readline
r, c = map(int,input().split())
array = []
for _ in range(r):
    array.append(input())

check = []
for i in range(c):
    string = ""
    for j in range(r):
        string += array[j][i]
    check.append(string)

breaking = 0
k = 0
cnt = -1
while True:
    dic = {}
    for i in range(c):
        if check[i][k:] in dic:
            breaking = 1
            break
        dic[check[i][k:]] = 1
    if breaking == 1:
        break
    cnt += 1
    k += 1
    if k == r:
        break
print(cnt)


        
