import math
from collections import deque
import copy
primeDictionary1 = {}
def primeNumber(num):
    if num == 2 or num == 3:
        return True
    elif num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for i in range(1000,10000):
    if primeNumber(i):
        primeDictionary1[i] = 1
    else:
        primeDictionary1[i] = 0

n = int(input())

for _ in range(n):
    st = list(map(int,input().split()))
    primeDictionary2 = copy.deepcopy(primeDictionary1)
    primeDictionary2[st[0]] = 0
    q = deque()
    start = str(st[0])
    q.append([start,0])
    end = str(st[1])
    cnt = 0
    check = False
    while q:
        start, cost = q.popleft()
        if start == end:
            print(cost)
            check = True
            break
        for i in range(4):
            # 0 1 2 3
            for j in range(0,10):
                number = start[0:i] + str(j) + start[i+1:4]
                if int(number) in primeDictionary2:
                    if primeDictionary2[int(number)] == 1:
                        primeDictionary2[int(number)] = 0
                        q.append([number,cost+1])
    if check == False:
        print('Impossible')
