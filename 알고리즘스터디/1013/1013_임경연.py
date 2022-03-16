import sys
import re

input = sys.stdin.readline

N = int(input())

pattern = re.compile("(100+1+|01)+")

words = []
for i in range(N):
    a = input().split()
    words.append(a[0])

for a in words:
    if re.fullmatch(pattern, a):
        print("YES")
    else:
        print("NO")
