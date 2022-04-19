from collections import defaultdict
import copy

# N_seq = defaultdict(list)
# N_rev_seq = defaultdict(str)

# M_seq = defaultdict(list)
# M_rev_seq = defaultdict(str)


# N = list(input())
# M = list(input())

# for i, j in enumerate(N):
#     N_seq[j].append(i)
#     N_rev_seq[i] = j

# for i, j in enumerate(M):
#     M_seq[j].append(i)
#     M_rev_seq[i] = j

# answer = 0
# for i in range(len(N)-1):
#     for j in M_seq[N_rev_seq[i]]:
#         length = 0
#         n = copy.deepcopy(i)
#         m = copy.deepcopy(j)
#         while True:
#             if N_rev_seq[n] == M_rev_seq[m] and n < len(N) and m < len(M):
#                 length += 1
#                 n += 1
#                 m += 1
#             else:
#                 answer = max(answer, length)
#                 break

# if answer == 1:
#     answer = 0
# print(answer)



N = input()
M = input()

dp = [[0] * (len(N) + 1) for _ in range(len(M) + 1)]

answer = 0
for i in range(1, len(M) + 1):
    for j in range(1, len(N) + 1):
        if N[j-1] == M[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])

print(answer)

    


