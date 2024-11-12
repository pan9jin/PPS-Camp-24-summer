import sys
input = sys.stdin.readline

n = int(input())
result, s_num, s, e = 0, 0, 0, 0

while e <= n:
    if s_num < n:
        e += 1
        s_num += e
    elif s_num > n:
        s_num -= s
        s += 1
    else:
        result += 1
        e += 1
        s_num += e
print(result)