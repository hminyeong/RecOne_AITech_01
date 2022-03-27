import sys


input = sys.stdin.readline

tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(left, right):
    if left > right:
        return 0
    
    else:
        a = right + 1
        for i in range(left+1, right+1):
            if tree[left] < tree[i]:
                a = i
                break
        
        postorder(left+1, a - 1)
        postorder(a, right)
        print(tree[left])

postorder(0, (len(tree) - 1))


