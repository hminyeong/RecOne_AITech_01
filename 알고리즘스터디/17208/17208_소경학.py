n, m, k = map(int,input().split())
store = []
for _ in range(n):
    store.append(list(map(int,input().split())))
dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
for t in range(n):
    x = store[t][0]
    y = store[t][1]
    for i in range(1,m+1):
        for j in range(1,k+1):
            if x <= i and y <= j:
                dp[t+1][i][j] = max(dp[t][i-x][j-y]+1,dp[t][i][j])
            else:
                dp[t+1][i][j] = dp[t][i][j]
print(dp[-1][-1][-1])

