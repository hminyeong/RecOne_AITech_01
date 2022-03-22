import sys

input = sys.stdin.readline

spines = []

for i in range(4):
    spines.append(list(input().split()[0]))

N = input()

def move(spine, direction, token, visited):
    if token == 0:
        return 0
    else:
        if direction == 1:
            a = spines[spine].pop()
            spines[spine].insert(0, a)

            left, right = spine - 1, spine + 1

            if 0 <= left and visited[left] == 0:
                if spines[left][2] != spines[spine][7]:
                    visited[left] = 1
                    move(left, -1, 1, visited)
                else:
                    move(left, -1, 0, visited)
            if right <= 3 and visited[right] == 0:
                if spines[right][6] != spines[spine][3]:
                    visited[right] = 1
                    move(right, -1, 1, visited)
                else:
                    move(right, -1, 0, visited)
        
    
        else:
            a = spines[spine].pop(0)
            spines[spine].append(a)

            left, right = spine - 1, spine + 1

            if 0 <= left and visited[left] == 0:
                if spines[left][2] != spines[spine][5]:
                    visited[left] = 1
                    move(left, 1, 1, visited)
                else:
                    move(left, 1, 0, visited)
            if right <= 3 and visited[right] == 0:
                if spines[right][6] != spines[spine][1]:
                    visited[right] = 1
                    move(right, 1, 1, visited)
                else:
                    move(right, 1, 0, visited)

for i in range(int(N)):
    s, d = map(int, input().split())
    s = s - 1
    visited = [0, 0, 0, 0]
    visited[s] = 1

    move(s, d, 1, visited)


answer = 0

for i, j in enumerate(spines):
    answer += int(j[0]) * 2**(i)

print(answer)



