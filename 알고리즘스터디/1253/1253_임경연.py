import sys

def solution(lst):
    answer = 0
    lst = sorted(lst)
    for i, j in enumerate(lst):
        tmp_lst = lst[:i] + lst[i+1:]
        l = 0
        r = len(tmp_lst) - 1
        while l < r:
            value = tmp_lst[l] + tmp_lst[r]
            if value == j:
                answer += 1
                break
            else:
                if value < j:
                    l += 1
                else:
                    r -= 1
    return answer


if __name__ == '__main__':
    N = int(input())
    lst = list(map(int, sys.stdin.readline().split()))
    ans = solution(lst)
    print(ans)