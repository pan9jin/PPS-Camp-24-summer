import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
s_num = [0]*(n+1)
for i in range(n):
    s_num[i+1] = s_num[i] + num[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(s_num[j] - s_num[i-1])