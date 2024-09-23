import sys
input = sys.stdin.readline

p, n = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
cnt = 0

for i in range(n):
    if p < 200:
        p+=l[i]
        cnt+=1
    else:
        break
print(cnt)