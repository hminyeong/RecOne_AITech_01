import sys


input = sys.stdin.readline

N, K = map(int, input().split())

def mean(lst):
    return sum(lst) / len(lst)

def validation(lst, mean):
    answer = 0
    for i in lst:
        answer += (i - mean)**2
    return (answer / len(lst))

p = list(map(int, input().split()))

answer = 10000000000000000000000000000000000000000000000

while K <= N:
    for j in range(N - K + 1):
        i = p[j:j+K]
        tmp_mean = mean(i)
        tmp = validation(i, tmp_mean)
        if tmp < answer:
            answer = tmp
    
    K += 1

print((answer)**(1/2))




