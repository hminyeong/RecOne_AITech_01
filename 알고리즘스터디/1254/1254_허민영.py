def p(idx):
    tmp = 0
    for _ in range(idx+tmp, L-tmp-1):
        if S[idx+tmp] != S[L-tmp-1]:
            return False
        tmp += 1
    return True
 
 
S = input()
L, result = len(S), 0

for i in range(L):
    if p(i):
        result = L + i
        break
    
print(result)

