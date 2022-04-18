# 합이 26

from collections import defaultdict


alphabet = ['x', 'A','B','C','D','E','F','G','H','I','J','K','L']

nums = defaultdict(int)
inverse_nums = defaultdict(str)

for i, j in enumerate(alphabet):
    nums[j] = i
    inverse_nums[i] = j

stars = [list(input()) for i in range(5)]

space = [(i, j) for i in range(5) for j in range(len(stars[0])) if stars[i][j] == 'x']

used = [stars[i][j] for i in range(5) for j in range(len(stars[0])) if stars[i][j] != 'x' and stars[i][j] != '.']

lines = [[(0, 4), (1, 3), (2, 2), (3, 1)], 
[(0, 4), (1, 5), (2, 6), (3, 7)], 
[(1, 1), (1, 3), (1, 5), (1, 7)],
[(1, 1), (2, 2), (3, 3), (4, 4)],
[(1, 7), (2, 6), (3, 5), (4, 4)],
[(3, 1), (3, 3), (3, 5), (3, 7)]]

# 1, 3
# 0, 4


def findValue(loc):
    y, x = loc
    possible = []
    max_value = 100
    for i in range(len(lines)):
        counts = 0
        if loc in lines[i]:
            for y, x in lines[i]:
                counts += nums[stars[y][x]]
            max_value = min(max_value, 26 - counts+1, len(alphabet))
    for i in range(1, max_value):
        if alphabet[i] not in used:
            possible.append(alphabet[i])
    return possible

flag = False

def dfs(count):
    global flag

    if flag:
        return

    if count == len(space):
        for i in stars:
            print("".join(i))
        flag = True
        return
    
    else:
        (i, j) = space[count]
        values = findValue((i, j))

        for num in values:
            stars[i][j] = num
            used.append(num)
            dfs(count+1)
            stars[i][j] = "x"
            used.pop()

dfs(0)


    
    
    
    


