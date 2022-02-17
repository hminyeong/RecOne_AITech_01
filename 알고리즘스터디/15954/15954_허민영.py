# 십진법(decimal)모듈은 실수를 표현하기 위하여 float자료형보다 정확한 Decimal클래스를 제공
# 편차 = 값 - 평균
# 분산 = 제곱의 평균 - 평균의 제곱 = 편차 제곱의 평균
# 표준 편차 = 분산의 제곱근

from decimal import Decimal

N, K = map(int, input().split())
N_list = list(map(int,input().split()))

sums = [0 for i in range(N+1)] # [0,0,0,0,0,0]
exps = [0 for i in range(N+1)] # [0,0,0,0,0,0]

for i in range(1, len(N_list)+1):
  sums[i] = sums[i-1] + N_list[i-1] # [0,1,3,6,10,15]
  exps[i] = exps[i-1] + N_list[i-1] ** 2 # [0,1,5,14,30,55]
  print(sums, exps)

re = Decimal('inf')

for i in range(K, N+1): # 3 4 5
  for j in range(N-i+1): # 0 1 2, 0 1, 0
    print(i,j)
    mean = Decimal(sums[i+j] - sums[j]) / i # 평균
    var = Decimal(exps[i+j] - exps[j]) / i - mean * mean # 분산
    re = min(re, var)

print(re.sqrt())

