import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

costs = [list(map(int, input().split())) for _ in range(m)]
print(costs)

# 최소 비용을 선택해야 하기 때문에 비용을 기준으로 오름차순 정렬 
costs.sort(key=lambda x: x[2])
print(costs)
print(costs[0][0])

# set 자료구조 이용
s = {costs[0][0]}

answer = 0

# set에 모든 컴퓨터가 들어오기전까지 돌리기
while len(s) != n:
    print(costs)
    for idx, cost in enumerate(costs):
        print(idx, cost)
        print()
        if cost[0] in s and cost[1] in s: # 양쪽 node가 이미 자료구조에 들어있다면 무시
            continue

        if cost[0] in s or cost[1] in s: # 둘중 하나의 노드만 들어가있을 경우    
            answer += cost[2] # 비용추가
            s.update([cost[0], cost[1]]) # set자료구조에 update(값 여러개 추가)반영
            
            # 한번 훑고 나온 노드 연결 정보는 -1로 바꿔서 다음번에 영향을 미치지 않게
            costs[idx] = [-1, -1, -1]
            
            # 최소비용을 담았으면 탈출하고 다시 처음부터 훑어서 방금 연결된 노드와 연결된 노드를 계속 찾음
            break

print(answer)
