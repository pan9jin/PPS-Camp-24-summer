import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

result, s_num = s[0], s[0]
for i in range(1, n):
    result = max(result, -s_num + s[i])
    s_num += s[i]
print(result)