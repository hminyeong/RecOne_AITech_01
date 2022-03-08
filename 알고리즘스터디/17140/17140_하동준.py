import sys
from collections import Counter
import numpy as np

input = sys.stdin.readline

r, c, k = map(int, input().split())

arr = [[0 for _ in range(10)] for _ in range(10)]
arr = np.array(arr)

for i in range(3):
    tmp = list(map(int, input().split()))
    for idx ,j in enumerate(tmp):
        arr[i][idx] = j

maxR, maxC = 3, 3

def RR(maxC, maxR, arr):
    for row in range(maxR):
        rowcnt = Counter(arr[row])
        del(rowcnt[0])
        rowcnt = sorted(rowcnt.items(), key=lambda x:(-x[1], x[0]))
        i=0
        for key,value in rowcnt:
            arr[row][i*2] = key
            arr[row][i*2+1] = value
            i += 1
        for j in range(i*2,len(arr)):
            arr[row][j]=0
        maxC = max(maxC, len(rowcnt)*2)


def CC(maxC, maxR, arr):
    liT = arr.transpose()
    print(liT)
    for row in range(maxC):
        rowcnt = Counter(liT[row])
        del(rowcnt[0])
        rowcnt = sorted(rowcnt.items(), key=lambda x:(-x[1], x[0]))
        # print(rowcnt)
        i=0
        # print(rowcnt)

        print(len(rowcnt))
        for key,value in rowcnt:
            liT[row][i*2] = key
            liT[row][i*2+1] = value
            i += 1
        for j in range(i*2,len(liT[0])):
            liT[row][j]=0
        maxR = max(maxC, len(rowcnt)*2)
        print(liT)
        arr = liT.transpose()


if(maxR >= maxC):
    RR(maxC, maxR, arr)
    # print(arr)

# if(maxR < maxC):
CC(maxC, maxR, arr)

print(arr)










# maxC=3

# li = [[0 for _ in range(10)] for _ in range(10)]
# li = np.array(li)

# li[0][0]=1
# li[0][1]=2
# li[0][2]=2

# li[1][0]=2
# li[1][1]=1
# li[1][2]=3

# li[2][0]=2
# li[2][1]=1
# li[2][2]=3


# # print(li)
# for row in range(3):
#     rowcnt = Counter(li[row])
#     del(rowcnt[0])
#     rowcnt = sorted(rowcnt.items(), key=lambda x:(-x[1], x[0]))
#     # print(rowcnt)
#     i=0
#     # print(len(rowcnt))
#     for key,value in rowcnt:
#         li[row][i*2] = key
#         li[row][i*2+1] = value
#         i += 1
#     for j in range(i*2,len(li[0])):
#         li[row][j]=0
#     maxC = max(maxC, len(rowcnt)*2)
# print(li)

# liT = li.transpose()
# print(liT)

# # rowcnt = Counter(liT[0])
# # del(rowcnt[0])

# for row in range(maxC):
#     rowcnt = Counter(liT[row])
#     del(rowcnt[0])
#     rowcnt = sorted(rowcnt.items(), key=lambda x:(-x[1], x[0]))
#     # print(rowcnt)
#     i=0
#     # print(len(rowcnt))
#     for key,value in rowcnt:
#         liT[row][i*2] = key
#         liT[row][i*2+1] = value
#         i += 1
#     for j in range(i*2,len(liT[0])):
#         liT[row][j]=0
#     maxC = max(maxC, len(rowcnt)*2)


# print(liT)


# # def CC():

# # li=[1,1,1,1,3,4,2,2,7,8,4,4]
# # li = Counter(li)
# # # print(cnt.keys())

# # rowcnt = sorted(li.items(), key=lambda x:(-x[1], x[0]))
# # print(rowcnt)

# li=list([[1,1,1],[2,2,2]])
# print(li[])
