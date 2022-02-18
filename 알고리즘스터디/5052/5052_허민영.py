import sys
input = sys.stdin.readline

def check():
    for i in range(len(num_list)-1):
        if num_list[i] == num_list[i+1][0:len(num_list[i])]: # 113, 123|40   12340, 12344|0
            return print('NO') 
    return print('YES')

t = int(input())

for _ in range(t):
    n = int(input())
    num_list = []
    for _ in range(n):
        num = input().strip() # 인자 없을 경우 양쪽 공백 제거
        num_list.append(num)
    num_list.sort()
    #print(num_list)
    check()
