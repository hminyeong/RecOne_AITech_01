'''
이분탐색(이진탐색)
O(log N)
데이터가 정렬되어 있어야 함
mid를 활용해서 매 연산마다 탐색하는 범위를 절반으로 좁혀 나감

투 포인터
O(N)
데이터가 정렬되어 있지 않아도 됨
양끝단에서 한칸씩 이동하면서 알맞는 값을 찾음
'''
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

def good_search(i, target):
    # 0이 포함되는 경우 자기 자신을 더하게 되기 때문에 자기 자신 제외
    temp = n_list[:i] + n_list[i+1:]
    left = 0
    right = n-2
    while left < right:
        sum = temp[left] + temp[right]
        if target > sum:
            left += 1
        elif target < sum:
            right -= 1
        else:
            return True

cnt = 0
for i in range(len(n_list)):
    if good_search(i, n_list[i]):
        cnt += 1
print(cnt)
