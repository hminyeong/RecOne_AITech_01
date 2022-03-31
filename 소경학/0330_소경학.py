n, m, k = map(int,input().split())
array = [[0 for _ in range(n+1)] for _ in range(n+1)]
check = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    array[a+1][b+1] = 1
    check[a+1][b+1] = 1

for i in range(2,n+1):
    array[i][1] += array[i-1][1]
for j in range(2,n+1):
    array[1][j] += array[1][j-1]
for i in range(1,n+1):
    for j in range(2,n+1):
        check[i][j] += check[i][j-1]

for i in range(2,n+1):
    for j in range(2,n+1):
        array[i][j] += array[i-1][j] + check[i][j-1]
answer = 0
# a b
# c d
# d = (a+b+c+d) - (a+b) - (a+c) + a
for i in range(m,n+1):
    for j in range(m,n+1):
        ABCD = array[i][j]
        AB = array[i-m][j]
        AC = array[i][j-m]
        A = array[i-m][j-m]
        answer = max(answer,(ABCD-AB-AC+A))
print(answer)

