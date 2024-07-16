import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
book = {}
for _ in range(n):
    b = input()
    if b not in book:
        book[b] = 1
    else:
        book[b] += 1

l = []
best = max(book.values())

for i in book:
    if best == book[i]:
        l.append(i)

l.sort()
print(l[0])