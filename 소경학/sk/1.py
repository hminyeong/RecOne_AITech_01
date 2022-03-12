def solution(money, costs):
    array = []
    check = [1,5,10,50,100,500]
    for i in range(6):
        array.append([costs[i]/check[i],check[i],costs[i]])
    array.sort()
    answer = 0
    for i in range(6):
        a = money // array[i][1] # 동전 개수
        money -= a*array[i][1] # 남은 금액
        answer += (a * array[i][2])

    
    return answer