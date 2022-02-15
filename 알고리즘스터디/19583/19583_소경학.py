s, e, q = input().split()
def change_time(time):
    x, y = time.split(":")
    return int(x)*60 + int(y)
answer = [change_time(s),change_time(e),change_time(q)]
array = []
while True:
    try:
        time, name = input().split()
        array.append([change_time(time),name])
    except:
        break
dic = {}
cnt = 0
for i in array:
    if i[0] <= answer[0]:
        dic[i[1]] = 1
    elif answer[1] <= i[0] < answer[2]:
        if i[1] in dic:
            cnt += 1
print(cnt)