import math

def primeNumber(num):
    if num == 2 or num == 3:
        return True
    elif num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def palindrome(num):
    array = str(num)
    if array == array[::-1]:
        return True
    else:
        return False

n = int(input())
for i in range(n,20000000):
    if primeNumber(i) and palindrome(i):
        print(i)
        break