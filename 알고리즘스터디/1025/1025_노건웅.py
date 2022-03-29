import sys
from functools import reduce
def input(): return sys.stdin.readline().rstrip()

def make_number(x1,x2):
    return x1*10 + x2

def check(r,c):
    nums = []
    for r_d in range(-max_d-1,max_d+1):
        for c_d in range(-max_d-1,max_d+1):
            for cnt in range(1,max(n,m)+1):
                num = [matrix[r+i*r_d][c+i*c_d] for i in range(cnt) if 0<= r+i*r_d < n and 0 <= c + i*c_d< m]
                if len(num) == cnt:
                    nums.append(reduce(make_number,num))
    result = -1
    for num in nums:
        if num in square_number and result < num:
            result = num
    return result

n,m = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(n)]
square_number = set([ num**2 for num in range(0,100001)])

max_d = max(n,m)
result = -1
for i in range(n):
    for j in range(m):
        temp = check(i,j)
        if result < temp:
            result = temp
print(result)
