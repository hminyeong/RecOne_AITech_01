import sys
word_list = []
while True:
    a = sys.stdin.readline().rstrip()
    if a == '-':
        break
    word_list.append(a)

check_list = []
while True:
    a = sys.stdin.readline().rstrip()
    if a == '#':
        break
    check_list.append(a)
for i in check_list:
    dic = {}
    for j in i:
        dic[j] = 0
        for k in word_list:
            if j in k:
                iff = True
                for l in k:
                    if k.count(l) > i.count(l):
                        iff = False
                        break
                if iff:
                    dic[j] += 1
    x = [x for x in dic if dic[x] == min(dic.values())]
    mn = min(dic.values())
    y = [y for y in dic if dic[y] == max(dic.values())]
    mx = max(dic.values())
    x.sort()
    y.sort()
    print("".join(x),mn,"".join(y),mx)
