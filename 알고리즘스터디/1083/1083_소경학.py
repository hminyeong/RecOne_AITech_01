n = int(input())
array = list(map(int,input().split()))
s = int(input())

def findMaxIdx(start,end):
    for i in range(start,end+1):
        if max(array[start:end+1]) == array[i]:
            return i

def changeIdx(maxIdx,targetIdx):
    array[targetIdx:maxIdx+1] = [array[maxIdx]] + array[targetIdx:maxIdx]
    return maxIdx-targetIdx

for i in range(n):
    idx = findMaxIdx(i,i+s)
    s -= changeIdx(idx,i)
    if s == 0:
        break
print(*array)