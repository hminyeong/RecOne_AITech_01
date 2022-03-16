import sys
input = sys.stdin.readline


def build_counter(s:str):
    rst = dict()
    for char in s:
        if char in rst: rst[char]+=1
        else: rst[char]=1
    return rst

def solution(words, tgt):

    possible = list()
    ans = dict()
    tgt = build_counter(tgt)
   
    # 가능한 단어만 뽑아보기
    for word in words:
        p = True
        word = build_counter(word)
        for char in word:
            if char not in tgt or word[char]>tgt[char]:
                p = False
                break
        if not p: continue
        possible.append(word)

    # puzzle 문자 하나씩 가운데로 보냈을 때, 가능한 단어들 찾기 
    for char in tgt:
        temp = 0
        for word in possible:
            if char not in word: # 중간 문자는 꼭 포함해야 하므로.
                continue
            temp += 1
        ans[char] = temp

    ans = ans.items()
    max_ = max(ans, key=lambda x:x[1])[1]
    min_ = min(ans, key=lambda x:x[1])[1]
    max_char, min_char = list(), list()
    for pair in ans:
        if pair[1]==max_: max_char.append(pair[0])
        if pair[1]==min_: min_char.append(pair[0])
    
    return [''.join(sorted(min_char)), str(min_), ''.join(sorted(max_char)), str(max_)]



def input_func(arr, sign):
    arr = []
    while True:
        input_value = input().strip()
        if input_value == sign:
            break

        arr.append(input_value)
    return arr


dictionary = input_func([], '-')
puzzles = input_func([], '#')

for puzzle in puzzles:
    print(' '.join(solution(dictionary, puzzle)))
