import copy
s = list(input())

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break