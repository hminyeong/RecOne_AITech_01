# 나머지가 0인 경우는 부분합이 m의 배수인 경우로 볼 수 있음
import sys
input = sys.stdin.readline

n, m = map(int,sys.stdin.readline().split())
n_lise = list(map(int,sys.stdin.readline().split()))

array = [0 for i in range(m)]
sum = 0
array[0] = 1

for i in range(n):
    sum += n_lise[i]
    array[sum % m] += 1

result=0
for i in array:
    result += i*(i-1)//2

print(result)