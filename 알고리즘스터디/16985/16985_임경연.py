from collections import deque
from copy import deepcopy
from itertools import permutations

ori_maze = []

for i in range(5):
    space = [[] for _ in range(5)]
    for j in range(5):
        space[j] += (list(map(int, input().split())))
    ori_maze.append(space)

move_x = [1, -1, 0, 0, 0, 0]
move_y = [0, 0, 1, -1, 0, 0]
move_z = [0, 0, 0, 0, 1, -1]


def rotate(space):
    N = len(space)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = space[r][c]
    
    return ret

def BFS():
    # 시작 : 0, 0, 0
    # 도착 : 4, 4, 4
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return 1e10

    q = deque()
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    q.append([0, 0, 0, 0])
    visited[0][0][0] = 1 # z, y, x 순
    

    while q:
        x, y, z, c = q.popleft()
        if x == 4 and y == 4 and z == 4:
            return c
        
        for i in range(6):
            x_, y_, z_ = move_x[i], move_y[i], move_z[i]
            m_x, m_y, m_z = x + x_, y + y_, z + z_
            if 0 <= m_x < 5 and 0 <= m_y < 5 and 0 <= m_z < 5:
                if maze[m_z][m_y][m_x] == 1 and visited[m_z][m_y][m_x] == 0:
                    visited[m_z][m_y][m_x] = 1
                    q.append([m_x, m_y, m_z, c+1])
    
    return 1e10



ans = 1e10

order = [0, 1, 2, 3, 4]
order_list = list(permutations(order, 5))

for i in order_list:
    maze = deepcopy(ori_maze)
    maze[0], maze[1], maze[2], maze[3], maze[4] = maze[i[0]], maze[i[1]], maze[i[2]], maze[i[3]], maze[i[4]]
    

    for _ in range(4):
        maze[0] = rotate(maze[0])
        for _ in range(4):
            maze[1] = rotate(maze[1])
            for _ in range(4):
                maze[2] = rotate(maze[2])
                for _ in range(4):
                    maze[3] = rotate(maze[3])
                    for _ in range(4):
                        maze[4] = rotate(maze[4])
                        answer = BFS()
                        ans = min(ans, answer)

if ans == 1e10:
    print(-1)
else:
    print(ans)


                    


