from re import L
import sys
from math import sqrt
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

primes = defaultdict(int)

def checkPrime(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for l in ['1', '3', '7', '9']:
                if checkPrime(int(str(i)+ str(j)+str(k)+str(l))):
                    primes[str(i)+ str(j)+str(k)+str(l)] = 1

f = [str(i) for i in range(1, 10)]
s = [str(i) for i in range(10)]
t = [str(i) for i in [1,3,7,9]]

answer = []

for i in range(N):
    visited = [0] * 10000
    X, Y = map(str, input().split())

    q = deque()
    visited[int(X)] = 1
    q.append((X, 0))

    while True:
        cur, count = q.popleft()
        if cur == Y:
            answer.append(count)
            break
        
        for i in f:
            cur_ = i + cur[1:]
            if primes[cur_] == 1 and visited[int(cur_)] == 0:
                q.append((cur_, count + 1))
                visited[int(cur_)] = 1
        for i in s:
            cur_ = cur[0] + i + cur[2:]
            if primes[cur_] == 1 and visited[int(cur_)] == 0:
                q.append((cur_, count + 1))
                visited[int(cur_)] = 1
        for i in s:
            cur_ = cur[:2] + i + cur[3]
            if primes[cur_] == 1 and visited[int(cur_)] == 0:
                q.append((cur_, count + 1))
                visited[int(cur_)] = 1
        for i in t:
            cur_ = cur[:3] + i
            if primes[cur_] == 1 and visited[int(cur_)] == 0:
                q.append((cur_, count + 1))
                visited[int(cur_)] = 1
        
        if not q:
            answer.append("Impossible")
            break


for i in answer:
    print(i)





