import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
p, s = 0, 0

for i in range(n//2):
    p += a[i]
    s += a[n-i-1]
if n % 2 == 1:
    p += a[n//2]
print(s, p)