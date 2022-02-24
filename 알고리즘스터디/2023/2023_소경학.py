import math
n = int(input())

def primeNumber(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
check = []
def DFS(v,checkNumber):
    if v == n:
        check.append(checkNumber)
        return
    for i in range(1,10):
        if primeNumber(int(str(checkNumber)+str(i))):
            DFS(v+1,int(str(checkNumber)+str(i)))
    
for i in range(1,10):
    if primeNumber(i):
        DFS(1,i)

for i in check:
    print(i)