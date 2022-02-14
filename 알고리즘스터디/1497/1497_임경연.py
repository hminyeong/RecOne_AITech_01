import sys
from itertools import combinations

input = sys.stdin.readline

g, s = map(int, input().split())

guitar = []

for _ in range(g):
    a, b = map(str, input().split(" "))

    b = b.replace('Y', '1')
    b = b.replace('N', '0')
    b = int(b, 2)
    guitar.append(b)
    
answer = 1000000
count = 0

for i in range(1, g + 1):
    tmp = list(combinations(guitar, i))
    for combi in tmp:
        a = "0b0"
        for _ in combi:
            a = bin(int(a, 2) | _)
        
        count_a = a.count("1")
        if count_a > count:
            count = count_a
            answer = i
        
        if count_a == count:
            if i < answer:
                answer = i

if count == 0:
    print(-1)

else:
    print(answer)
        

