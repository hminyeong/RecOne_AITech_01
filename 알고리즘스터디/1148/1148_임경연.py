import sys
from collections import Counter, defaultdict
    

input = sys.stdin.readline

words = []
characters = []

while True:
    word = input().split()
    if word[0] == "-":
        break
    else:
        words.append(word[0])

while True:
    character = input().split()
    if character[0] == "#":
        break
    else:
        characters.append(character[0])

words_c = []
cha_c = []

for i in words:
    words_c.append(Counter(i))
for i in characters:
    cha_c.append(Counter(i))

# 단어 확인


for cha in cha_c:
    answer = defaultdict(int)
    for word in words_c:
        token = 0
        for i in word:
            if word[i] > cha[i]:
                token = 1
                break
        if token == 0:
            for i in word:
                answer[i] += 1

    for i in cha:
        if answer[i] != 0:
            continue
        else:
            answer[i] = 0

    min_value = min(answer.values())
    max_value = max(answer.values())
    
    min_ans = []
    max_ans = []
    for key, value in answer.items():
        if value == min_value:
            min_ans.append(key)
        if value == max_value:
            max_ans.append(key)
    min_ans = sorted(min_ans)
    max_ans = sorted(max_ans)
    print("".join(min_ans), int(min_value), "".join(max_ans), int(max_value))


