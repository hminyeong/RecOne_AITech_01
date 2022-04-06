import copy
n = int(input())
p = list(map(int,input().split()))
s = list(map(int,input().split()))
cnt = 0
check = copy.deepcopy(p)
while cnt < 500000:
    trust = True
    for i in range(0,n,3):
        if check[i] == 0 and check[i+1] == 1 and check[i+2] == 2:
            continue
        else:
            trust = False
    if trust:
        break
    for i in range(len(p)):
        check[s[i]] = p[i]
    cnt += 1
    p = copy.deepcopy(check)
    

if cnt == 500000:
    print(-1)
else:
    print(cnt)


