import math
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
array = list(map(int,input().split()))


def find_std(n_list):
    mean = sum(n_list) / len(n_list)
    variance = 0
    for i in n_list:    
        variance += (i-mean)**2
    variance = variance / len(n_list)
    return math.sqrt(variance)
answer = 99999999999
for i in range(k,n+1):
    for j in range(0,n-i+1):
        answer = min(answer,find_std(array[j:j+i]))
print(answer)
