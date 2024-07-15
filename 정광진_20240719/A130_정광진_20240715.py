import sys
input = sys.stdin.readline
k = int(input())
l = []
for _ in range(k):
    n = int(input())
    if l and n == 0:
        l.pop()
    else:
        l.append(n)
print(sum(l))