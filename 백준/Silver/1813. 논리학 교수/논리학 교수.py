import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

result = -1
for i in range(n+1):
    cnt = t.count(i)
    if cnt == i:
        result = max(result, i)

print(result)