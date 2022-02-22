import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
    if s == 0: 
        break
    Max = n_list[i] # 3
    change = 0
    for j in range(i+1,n):
        move = j-i
        if n_list[j] > Max:
            Max = n_list[j]
            change = move
        if move >= s:
            break
    if change:
        s -= change #교환한 만큼 빼줌
        n_list.remove(Max)
        n_list.insert(i, Max)
    print(change, n_list)

for i in n_list:
    print(i, end = ' ')
                
