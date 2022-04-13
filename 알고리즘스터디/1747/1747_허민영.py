import math

def isprime(x): #소수 판별
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

n = int(input())

result = 0
for i in range(n,1000001): # n ~ 최대값까지
    if i==1:
        continue
    #팰린드롬이면
    if str(i) == str(i)[::-1]:
        if isprime(i) == True: #소수 판별
            result = i
            break
if result == 0: #최대값보다 클 경우
    result = 1003001
print(result)