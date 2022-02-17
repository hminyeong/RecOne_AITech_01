import sys
from decimal import *
import math


input = sys.stdin.readline

N, K = map(int, input().split())

getcontext().prec = 28


p = list(map(Decimal, input().split()))

answer = Decimal('inf')

for i in range(N-K+1):
    sum_ = sum(p[i:i+K-1])
    sum_2 = sum(_**2 for _ in p[i:i+K-1])

    for j in range(K,N-i+1):
        sum_ += p[i+j-1]
        sum_2 += p[i+j-1]**2

        aver = sum_ / Decimal(j)
        std = ((sum_2 / Decimal(j)) - aver**2).sqrt()

        answer = min(answer, std)

print(answer)



