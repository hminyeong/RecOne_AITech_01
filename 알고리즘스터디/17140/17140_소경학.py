import copy

def R(array):
    mx_row = 0
    for i in range(len(array)):
        nlist = []
        mlist = []
        a = set(array[i])
        for j in a:
            if j == 0:
                continue
            nlist.append([array[i].count(j),j])
        nlist.sort()
        for j in nlist:
            mlist.append(j[1])
            mlist.append(j[0])
        mx_row = max(mx_row,len(mlist))
        if len(mlist) > 100:  
            array[i] = copy.deepcopy(mlist[:100])
        else:
            array[i] = copy.deepcopy(mlist)
    if mx_row > 100:
        mx_row = 100
    for i in range(len(array)):
        for _ in range(mx_row-len(array[i])):
            array[i].append(0)
    return array

def rotate(array):
    answer = []
    for i in range(len(array[0])):
        check = []
        for j in range(len(array)):
            check.append(array[j][i])
        answer.append(check)
    return answer
r,c,k = map(int,input().split())
array = []
for _ in range(3):
    array.append(list(map(int,input().split())))
cnt = 0
while True:
    if len(array) >= r and len(array[0]) >= c:
        if array[r-1][c-1] == k:
            break
    if len(array) >= len(array[0]):
        R(array)
    else:
        array = rotate(array)
        R(array)
        array = rotate(array)
    cnt += 1
    if cnt > 100:
        break
    
if cnt > 100:
    print(-1)
else:
    print(cnt)