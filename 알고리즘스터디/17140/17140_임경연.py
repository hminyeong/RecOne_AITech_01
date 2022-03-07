import sys
from collections import defaultdict

input = sys.stdin.readline

r, c, k = map(int, input().split())

a = []

for i in range(3):
    a.append(list(map(int, input().split())))

def R(a):
    length = 0
    answer = []
    for i in range(len(a)):
        b = defaultdict(int)
        a[i] = sorted(a[i])
        for j in range(len(a[i])):
            b[a[i][j]] += 1

        b = sorted(b.items(), key=lambda x: x[1])
        tmp = []
        for j in b:
            if j[0] == 0:
                continue
            tmp.append(j[0])
            tmp.append(j[1])
        
        tmp = tmp[:100]
        length = max(length, len(tmp))
        answer.append(tmp)
    
    for i in range(len(answer)):
        answer[i] = answer[i] + [0] * (length - len(answer[i]))
    
    return answer

def C(a):
    b = []
    for i in range(len(a[1])):
        tmp = []
        for j in range(len(a)):
            tmp.append(a[j][i])
        b.append(tmp)
    a = R(b)
    b = []
    for i in range(len(a[1])):
        tmp = []
        for j in range(len(a)):
            tmp.append(a[j][i])
        b.append(tmp)
    return b

time = 0
for i in range(101):
    try:
        if a[r-1][c-1] == k:
            print(time)
            break
    
        if len(a) >= len(a[0]):
            a = R(a)
        else:
            a = C(a)
        time += 1
    except:
        if len(a) >= len(a[0]):
            a = R(a)
        else:
            a = C(a)
        time += 1


if time == 101:
    print(-1)





