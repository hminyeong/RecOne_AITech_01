from math import sqrt

N = int(input())

def palindrome(n):
    return str(n) == str(n)[::-1]

def decimal(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    
    return True


while True:
    if N == 1:
        print(2)
        break
    if palindrome(N):
        if decimal(N):
            print(N)
            break
    
    N += 1