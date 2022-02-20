import sys

input = sys.stdin.readline

N, M = map(int, input().split())

m = list(map(int, input().split()))
w = list(map(int, input().split()))

m.sort()
w.sort()

answer = 0

def matching(N, M, big, small):
    dp = [[0] * N for _ in range(M)]
    dp[0][0] = abs(big[0] - small[0])
    for i in range(1, N - (M - 1)):
        dp[0][i] = min(abs(small[0] - big[i]), dp[0][i - 1])
    
    print(dp)

    for i in range(1, M):
        for j in range(1, N - (M - i - 1)):
            if i == j:
                dp[i][j] = dp[i-1][j-1] + abs(small[i] - big[j])
            else:
                dp[i][j] = min(dp[i-1][j-1] + abs(small[i]- big[j]), dp[i][j-1])
            print(dp, i, j)
    print(dp)
    return dp[M-1][N-1]
    

if N > M:
    print(matching(N, M, m, w))

else:
    print(matching(M, N, w, m))