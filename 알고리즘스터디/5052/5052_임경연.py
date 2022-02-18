import sys

input = sys.stdin.readline

N = int(input())

answer = []

for i in range(N):
    M = int(input())

    lst = []

    for i in range(M):
        lst.append(str(input())[:-1])
    
    lst.sort()

    for i, j in enumerate(lst):
        if i == len(lst) - 1:
            answer.append("YES")
            continue

        if j == lst[i+1][:len(j)]:
            answer.append("NO")
            break

for i in answer:
    print(i)