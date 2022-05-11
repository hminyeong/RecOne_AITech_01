def solution(lines):
    array = []
    for i in lines:
        a,b,c = i.split(" ")
        c = float(c[:-1])
        c *= 1000
        c = int(c)
        b1,b2,b3 = b.split(":")
        b1 = int(b1)
        b2 = int(b2)
        b3 = float(b3)
        b3 *= 1000
        b3 = int(b3)
        end = b1*3600000 + b2*60000 + b3
        kk = 1
        start = end - c + kk
        array.append([start,end])
    mx = 1
    for i in range(len(array)):
        count = 0
        count2 = 0
        count3 = 0
        for j in range(len(array)):
            if (array[i][0] <= array[j][0] < array[i][0] + 1000) or (array[i][0] <= array[j][1] <= array[i][0] + 1000) or (array[j][0]<=array[i][0] and array[j][1] >= array[i][1]):
                count += 1
            if (array[i][1] <= array[j][0] < array[i][1] +1000) or (array[i][1] <= array[j][1] <= array[i][1] + 1000) or (array[j][0]<=array[i][0] and array[j][1] >= array[i][1]):
                count2 += 1
            
        mx = max(mx,count,count2,count3)
    print(array)
    return mx