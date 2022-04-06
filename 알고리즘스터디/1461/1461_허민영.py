import sys
input = sys.stdin.readline

n,m = map(int, input().split())

books = list(map(int, input().split()))
books.sort()

abs_books = []

minus_count = 0
plus_count = 0
for i in range(len(books)):
    if books[i] < 0:
        minus_count += 1
    else:
        plus_count += 1
    abs_books.append((i, abs(books[i])))

abs_books.sort(key=lambda x:x[1], reverse=True)

minus = books[0]
plus = books[-1]

max_val = abs_books[0][1]

if m >= minus_count and m >= plus_count:
    min_val = min(abs(minus), abs(plus))
    max_val = max(abs(minus), abs(plus))
    print(2*min_val + max_val)
    exit()

minus_books = books[:minus_count]
plus_books = books[minus_count:]
plus_books.sort(reverse=True)

cnt = 0
answer = 0
for i in minus_books:
    print(cnt,i, answer)
    if cnt==0:
        answer += 2*abs(i)
    if cnt == m-1:
        cnt = 0
    else:
        cnt += 1

cnt = 0
for i in plus_books:
    print(cnt, i, answer)
    if cnt==0:
        answer += 2*abs(i)
    if cnt == m-1:
        cnt = 0
    else:
        cnt += 1

print(answer-max_val)
