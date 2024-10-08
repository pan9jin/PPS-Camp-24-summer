import sys
input = sys.stdin.readline

wj = list(map(int, input().split()))
sg = list(map(int, input().split()))

s1, s2 = 0, 0
result = False
for i in range(9):
    s1 += wj[i]
    if s1 > s2:
        result = True
    s2 += sg[i]
print('Yes' if result and s1 < s2 else 'No')