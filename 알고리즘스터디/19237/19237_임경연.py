# from collections import defaultdict
# from copy import deepcopy


# N, M, K = map(int, input().split())

# space = []
# shark_position = defaultdict(list)
# for i in range(N):
#     a = list(map(int, input().split()))
#     for j, k in enumerate(a):
#         if k != 0:
#             shark_position[k] = (j, i)
#     space.append(a)



# move = {1:(0, -1), 2: (0, 1), 3:(-1, 0), 4: (1, 0)}
# # 순서는 (0, -1) (0, 1) (-1, 0) (1, 0)

# dir_shark = list(map(int, input().split()))

# move_shark = []

# for i in range(M):
#     move_tmp = []
#     for j in range(4):
#         move_tmp.append(list(map(int, input().split())))
#     move_shark.append(move_tmp)



# def moving_shark(shark_num, time):
#     x, y = shark_position[shark_num]
#     d = dir_shark[shark_num-1]
#     token = 0

#     for i in move_shark[shark_num-1][d-1]:
#         dx, dy = move[i]
#         m_x, m_y = x + dx, y + dy
#         if m_x < 0 or m_x >= N or m_y < 0 or m_y >= N:
#             continue
#         if space[m_y][m_x] == 0 or time - space[m_y][m_x]%10000 > K:
#             return [x,y], [m_x, m_y], i
        
#         elif space[m_y][m_x] // 10000 == shark_num and token == 0:
#             back_position = [m_x, m_y]
#             back_direction = i
#             token = 1
#     return [x, y], back_position, back_direction
    
# time = 0
# live_shark = [i for i in range(1, M + 1)]


# while time < 1000 and len(live_shark) != 1:
#     time += 1
#     copy_live_shark = deepcopy(live_shark)
#     now_pos = []
    
#     for i in copy_live_shark:
#         pre, next, direction = moving_shark(i, time)
#         if next in now_pos:
#             space[pre[1]][pre[0]] = i * 10000 + time - 1
#             live_shark.remove(i)
#             continue
#         space[pre[1]][pre[0]] = i * 10000 + time - 1
#         now_pos.append(next)
#         shark_position[i] = next
#         dir_shark[i-1] = direction

# if time == 1000:
#     print(-1)
# else:
#     print(time)
        

from collections import defaultdict
from copy import deepcopy


N, M, K = map(int, input().split())

space = []
shark_position = defaultdict(list)
for i in range(N):
    a = list(map(int, input().split()))
    for j, k in enumerate(a):
        if k != 0:
            shark_position[k] = (j, i)
    space.append(a)



move = {1:(0, -1), 2: (0, 1), 3:(-1, 0), 4: (1, 0)}
# 순서는 (0, -1) (0, 1) (-1, 0) (1, 0)

dir_shark = list(map(int, input().split()))

move_shark = []

for i in range(M):
    move_tmp = []
    for j in range(4):
        move_tmp.append(list(map(int, input().split())))
    move_shark.append(move_tmp)




    
count = 0
live_shark = [i for i in range(1, M + 1)]
now_pos = []


while count < 1001 and len(live_shark) != 1:
    count += 1
    copy_live_shark = deepcopy(live_shark)
    prev_pos = deepcopy(now_pos)
    now_pos = []
    
    for i in copy_live_shark:
        x, y = shark_position[i]
        d = dir_shark[i-1]
        token = 0
        for j in move_shark[i-1][d-1]:
            dx, dy = move[j]
            m_x, m_y = x + dx, y + dy
            if m_x < 0 or m_x >= N or m_y < 0 or m_y >= N:
                continue
            if (space[m_y][m_x] == 0 or count - space[m_y][m_x]%10000 > K) and [m_x, m_y] not in prev_pos:
                pre, next, direction = [x,y], [m_x, m_y], j
                token = 2
                break
        
            elif space[m_y][m_x] // 10000 == i and token == 0:
                back_position = [m_x, m_y]
                back_direction = j
                token = 1
        if token == 1:
            pre, next, direction = [x, y], back_position, back_direction
        
        if next in now_pos:
            space[pre[1]][pre[0]] = i * 10000 + count - 1
            live_shark.remove(i)
            continue
        space[pre[1]][pre[0]] = i * 10000 + count - 1
        now_pos.append(next)
        shark_position[i] = next
        dir_shark[i-1] = direction
        
if count == 1001:
    print(-1)
else:
    print(count)
        

    