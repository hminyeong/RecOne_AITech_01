import sys
input = sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
deq=[deque(), deque()] # 도도, 수연
deomi=[deque(),deque()] # 도도, 수연

for i in range(n): # 게임을 위한 카드 셋팅
    a,b=map(int,input().split())
    deq[0].appendleft(a) # 도도 덱에 카드 추가
    deq[1].appendleft(b) # 수연 덱이 카드 추가

t=0 # 도도
for _ in range(m): #게임 실행 횟수 m번
    deomi[t].appendleft(deq[t].popleft()) #도도 덱 -> 도도 더미로 카드 이동
    if not deq[t]: # 게임 진행 도중 둘 중 하나라도 덱이 0이 되면 게임종료
        break
    win=-1
    for i in [0,1]:
        if deomi[i] and deomi[i][0]==5: # 도도 더미 맨위, 수연 더미 맨위 중 하나가 5면
            win=0 # 도도가 종침
    if deomi[0] and deomi[1] and deomi[0][0]+deomi[1][0]==5: 
            win=1 # 수연이가 종침
    if win!=-1: # 누군가 종을 쳤으니까
        for i in [1-win,win]: # 도도가 종쳤으면 1,0, (수연이가 종쳤으면 0,1)
            while deomi[i]: # 수연(도도)이 더미에서 카드 다 가져와서 도도(수연) 더미로 이동

                deq[win].append(deomi[i].pop())
    t=1-t

if len(deq[0])>len(deq[1]): # 도도 덱 카드 수 > 수연 덱 카드 수
    print('do')
elif len(deq[1])>len(deq[0]): # 수연 덱 카드 수 > 도도 덱 카드 수
    print('su')
else:
    print('dosu')
