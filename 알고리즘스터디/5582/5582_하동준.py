#%%
import sys
# import numpy as np

input= sys.stdin.readline
temp1 = input().strip()
temp2 = input().strip()
if(len(temp1) > len(temp2)):
    long_line = temp1
    len_long = len(long_line)
    short_line = temp2
    len_short = len(short_line)
else:
    long_line = temp2
    len_long = len(long_line)
    short_line = temp1
    len_short = len(short_line)
del temp1, temp2

table = [[False for _ in range(len_long)] for _ in range(len_short)]
for s_idx, s in enumerate(short_line):
    for l_idx, l in enumerate(long_line):
        if s==l:
            table[s_idx][l_idx] = True

num = len_long + len_short
start_list=[]
for i in range(len_short):
    start_list.append([i, 0])
for j in range(1,len_long):
    start_list.append([0,j])

result = 0
for i in start_list:
    cnt = 0
    row = i[0]
    col = i[1]
    while row < len_short and col < len_long:
        if(table[row][col] == True):
            cnt += 1
        else:
            cnt = 0
        row += 1
        col += 1
        result = max(cnt, result)
        

print (result)
