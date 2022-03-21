from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
do_deck = deque()
su_deck = deque()
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    do_deck.append(a)
    su_deck.append(b)
do = 0
su = 0
do_gnd = deque()
su_gnd = deque()

for i in range(m):
    if i % 2 == 0:
        do = do_deck.pop()
        do_gnd.append(do)
    else:
        su = su_deck.pop()
        su_gnd.append(su)
    if len(do_deck) == 0 or len(su_deck) == 0:
        break

    if su == 5 or do == 5:          
        if su_gnd:
            do_deck.extendleft(su_gnd)
            su = 0
            su_gnd = deque()
        if do_gnd:
            do_deck.extendleft(do_gnd)
            do = 0
            do_gnd = deque()
    elif do + su == 5 and do > 0 and su > 0:
        if do_gnd:
            su_deck.extendleft(do_gnd)
            do = 0
            do_gnd = deque()
        if su_gnd:
            su_deck.extendleft(su_gnd)
            su = 0
            su_gnd = deque()
    
# print(do_deck,su_deck)
if len(su_deck) == len(do_deck):
    print('dosu')
elif len(su_deck) > len(do_deck):
    print('su')
elif len(su_deck) < len(do_deck):
    print('do')