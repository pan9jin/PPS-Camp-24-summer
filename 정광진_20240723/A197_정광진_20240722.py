import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {i: i for i in range(1, n+1)}
for _ in range(m):
    i, j = map(int, input().split())
    dic[i], dic[j] = dic[j], dic[i]
print(*dic.values())