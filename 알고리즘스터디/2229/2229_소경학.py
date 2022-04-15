n = int(input())
array = list(map(int,input().split()))

dp = [0 for _ in range(n)]
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if j == 0:
            dp[i] = max(dp[i],max(array[:i+1])-min(array[:i+1]))
        else:
            dp[i] = max(dp[i], dp[j-1] + max(array[j:i+1]) - min(array[j:i+1]))
print(dp[-1])