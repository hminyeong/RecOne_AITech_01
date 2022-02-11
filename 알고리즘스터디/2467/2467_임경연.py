import sys

def findLiquid(lst):
    a = 0
    b = len(lst) - 1
    answer = [abs(lst[a] + lst[b]), (lst[a], lst[b])]


    while a < b:
        tmp_answer = lst[a] + lst[b]
        if tmp_answer == 0:
            return lst[a], lst[b]

        else:
            if abs(tmp_answer) < answer[0]:
                answer[0] = abs(tmp_answer)
                answer[1] = (lst[a], lst[b])
            if tmp_answer < 0:
                a += 1
            else:
                b -= 1
    return answer[1]

if __name__ == '__main__':
    n = map(int,sys.stdin.readline().split())
    lst = list(map(int,sys.stdin.readline().split()))
    ans = findLiquid(lst)
    print("{} {}".format(ans[0],ans[1]))