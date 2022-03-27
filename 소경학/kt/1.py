def solution(h, w, books):
    array = [[0 for _ in range(w)] for _ in range(h)]
    time = 1
    idx = 0
    answer = [0 for _ in range(len(books))]
    while True:
        if time > 105:
            break
        for i in range(idx,len(books)): 
            if books[i][1] != time:
                idx = i
                break
            check = 0
            for j in range(h): 
                for k in range(w-books[i][0]+1):
                    count = 0
                    for l in range(books[i][0]): 
                        if array[j][k+l] == 0:
                            count += 1
                        else:
                            break
                    if count == books[i][0]:
                        for l in range(books[i][0]):
                            array[j][k+l] = books[i][2]
                        check = 1
                        break
                    if check == 1:
                        break
                if check == 1:
                    break
            if check == 1:
                answer[i] = 1
        time += 1
        for i in range(h):
            for j in range(w):
                if array[i][j] == time:
                    array[i][j] = 0

    return answer