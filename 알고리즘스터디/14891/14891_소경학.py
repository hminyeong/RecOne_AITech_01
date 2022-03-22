from collections import deque

array = deque()
for _ in range(4):
    a = deque(input())
    array.append(a)
k = int(input())
rotation = []
for _ in range(k):
    a,b = map(int,input().split())
    rotation.append([a-1,b])

def rotate(num,direction):
    if direction == 1:
        array[num].appendleft(array[num].pop())
    elif direction == -1:
        array[num].append(array[num].popleft())

for i in rotation:
    check = [0,0,0,0]
    check[i[0]] = i[1]
    for j in range(i[0],0,-1):
        if array[j][6] == array[j-1][2]:
            check[j-1] = 0
        else:
            check[j-1] = check[j]*-1
    for j in range(i[0],3):
        if array[j][2] == array[j+1][6]:
            check[j+1] = 0
        else:
            check[j+1] = check[j] *-1
    for i in range(4):
        rotate(i,check[i])

answer = 0
if array[0][0] == '1':
    answer += 1
if array[1][0] == '1':
    answer += 2
if array[2][0] == '1':
    answer += 4
if array[3][0] == '1':
    answer += 8
print(answer)
