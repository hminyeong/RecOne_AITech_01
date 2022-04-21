N, M = map(int, input().split())

nums = list(map(int, input().split()))


sums, cnt = 0, [0] * M

for i in range(N):
    sums = (sums + nums[i]) % M
    cnt[sums] += 1

answer = 0

# 나머지가 같은 값은 구간 합 구간이 있다면 (ex. [1, A], [1, B]), 그 사이 구간은 M으로 나누어 떨어짐 ([A+1, B] % M == 0)
# 따라서 나머지가 같은 구간 2개를 선택하는 개수와 같음 (nC2)
# 나머지가 0인 경우 그 자체만 선택하는 경우가 있으므로 n을 한번 더 더해줘야 함

for i in range(M):
    if i == 0:
        answer += cnt[i] * (cnt[i] + 1) / 2
    else:
        answer += cnt[i] * (cnt[i] - 1) / 2

print(int(answer))


