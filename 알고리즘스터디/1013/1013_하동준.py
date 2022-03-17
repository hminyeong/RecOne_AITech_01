import re
import sys
 
T = int(sys.stdin.readline())
results = []
 
for _ in range(T):
    sign = sys.stdin.readline().replace('\n', '')
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    # 전체 매치 확인
    if m: results.append("YES")
    else: results.append("NO")
 
for result in results:
    sys.stdout.write(str(result)+'\n')
