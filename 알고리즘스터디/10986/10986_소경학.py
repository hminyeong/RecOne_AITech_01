from collections import Counter
n, m = map(int,input().split())
array = list(map(int,input().split()))
for i in range(1,n):
    array[i] += array[i-1]
answer = 0
for i in range(n):
    array[i] = array[i] % m
dic = Counter(array)
for i in dic:
    if dic[i] > 1:
        answer += (dic[i] * (dic[i]-1)) // 2
for i in array:
    if i % m == 0:
        answer += 1
print(answer)