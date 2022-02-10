n = int(input())
array = list(map(int,input().split()))
startIdx = 0
endIdx = n-1
answerNumber1 = array[startIdx]
answerNumber2 = array[endIdx]
answerSum = array[startIdx] + array[endIdx]
while True:
    if array[startIdx]+array[endIdx] <= 0:
        startIdx += 1
        if startIdx >= endIdx:
            break
        if abs(answerSum) > abs(array[startIdx]+array[endIdx]):
            answerNumber1 = array[startIdx]
            answerNumber2 = array[endIdx]
            answerSum = array[startIdx]+array[endIdx]
    else:
        endIdx -= 1
        if startIdx >= endIdx:
            break
        if abs(answerSum) > abs(array[startIdx]+array[endIdx]):
            answerNumber1 = array[startIdx]
            answerNumber2 = array[endIdx]
            answerSum = array[startIdx]+array[endIdx]

print(min(answerNumber1,answerNumber2), max(answerNumber1,answerNumber2))