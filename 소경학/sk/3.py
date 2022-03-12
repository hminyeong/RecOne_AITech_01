def solution(width, height, diagonals):
    n = width
    m = height
    answer = 0
    array = [[0 for _ in range(m+1)] for _ in range(n+1)]
    array[0][0] = 0
    for i in range(1,m+1):
        array[0][i] = 1
    for i in range(1,n+1):
        array[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            array[i][j] = array[i-1][j] + array[i][j-1]
    for i in diagonals:
        x1,y1 = i[0]-1, i[1]
        x2,y2 = i[0], i[1]-1
        first1, first2 = array[x2][y2], array[x1][y1]
        second1, second2 = array[n-x1][m-y1], array[n-x2][m-y2]
        answer += (first1 * second1)
        answer += (first2 * second2)
    answer %= 10000019
    return answer