import sys
sys.setrecursionlimit(10**6)

num_list=[]
while True:
    try:
        num=int(input())
        num_list.append(num)
    except:
        break



def traverse(left,right):
    #순서 역전시 종료
    if left>right:
        return
    else:
        mid=right+1        #분할 기준
        for i in range(left+1,right+1):
            #해당 원소가 현재 노드보다 크다면 그 전까지는 왼쪽 서브 트리,
            #해당 원소 이후는 오른쪽 서브 트리이다.
            # 50 30 24 5 28 45 98 52 60
            # root left right
            # 50| 30 24 5 28 45 |98 52 60
            # 30| 24 5 28| 45
            # 24| 5 |28
            # 98| 52 60
            # 52| none|60
            if num_list[left]<num_list[i]:
                mid=i
                break
        traverse(left+1,mid-1)
        traverse(mid,right)
        print(num_list[left])

traverse(0,len(num_list)-1)