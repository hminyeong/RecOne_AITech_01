n = int(input())
array = list(map(int,input().split()))
total = 0
def checking(start,end):
    if start > end:
        div = (array[start]-array[end]) / (start-end)
        for i in range(end+1,start):
            div2 = (array[start]-array[i]) / (start-i)
            if div2 <= div or (div>=0 and div2<=0):
                return False
    elif start == end:
        return False
    else:
        div = (array[end]-array[start]) / (end-start)
        for i in range(start+1,end):
            div2 = (array[i]-array[start]) / (i-start)
            if div2 >= div or (div<=0 and div2>=0):
                return False
    return True
for i in range(len(array)):
    cnt = 0
    for j in range(len(array)):
        if checking(i,j):
            cnt += 1
    total = max(cnt,total)
print(total)