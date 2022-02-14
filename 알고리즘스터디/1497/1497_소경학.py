from itertools import combinations
from tkinter.tix import Tree
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(input().split()))
answer = -1
cnt = 0
for i in range(1,n+1):
    n_list = list(combinations(array,i))
    for j in range(len(n_list)):
        check = [False for _ in range(m)]
        for k in n_list[j]:
            for l in range(m):
                if k[1][l] == 'Y':
                    check[l] = True
        if check.count(True) > cnt:
            answer = i
            cnt = check.count(True)
print(answer)
        