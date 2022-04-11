import sys

input = sys.stdin.readline
N, M = map(int,input().split())
# print(a+b)
books = list(map(int, input().split()))
books.sort()
# print(books)
plus_books = []
minus_books = []

for i in books:
    if i < 0:
        minus_books.append(i)
    else:
        plus_books.append(i)
plus_books.sort(reverse=True)

# 절대값 높은 순으로 정렬
# print(plus_books)
# print(minus_books)

print(int(len(minus_books)/M) + 1)

tt = []
for i in range(len(minus_books)):
    if i%M == 0:


# print(3%2)