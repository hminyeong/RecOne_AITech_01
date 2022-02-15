import sys
import re

timetable = []

input = sys.stdin.readline
s, e, q = input().split()
s = int(re.sub(':', '', s))
e = int(re.sub(':', '', e))
q = int(re.sub(':', '', q))


cond1, cond2 = set(), set()

while True:
    try:
        t, person = input().split()
        t = int(re.sub(':', '', t))

        if(t <= s):
            cond1.add(person)
        if(e <= t <= q):
            cond2.add(person)
    except:
        break
print(len(cond1 & cond2))
