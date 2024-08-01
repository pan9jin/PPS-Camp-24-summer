import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
cnt = 0
for s in size:
    cnt += (s//t + 1)
    if s%t == 0:
        cnt-=1
print(cnt)
print(n//p, n%p)