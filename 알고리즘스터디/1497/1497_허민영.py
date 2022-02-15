from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 기타개수, 곡개수
array = []

for _ in range(n):
    array.append(list(input().split()))
    #print('array: ', array)
    
answer = -1 # 연주할 수 있는 곡 없으면 -1 출력
cnt = 0

for i in range(1,n+1):
    n_list = list(combinations(array,i))
    #print('n_list: ', n_list)
    
    for j in range(len(n_list)): #기타개수만큼
        check = [False for _ in range(m)]
        #print(check)
        
        for k in n_list[j]:
            for l in range(m):
                if k[1][l] == 'Y':
                    check[l] = True # False -> True
                    #print(check)
                    
        if check.count(True) > cnt: # 연주 가능한 곡이 더 많아지면
            answer = i # 기타 개수 업데이트
            cnt = check.count(True) # 연주 가능한 곡 개수 업데이트
            #print(check.count(True), answer, cnt)
            
print(answer)
