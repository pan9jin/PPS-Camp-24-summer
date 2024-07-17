import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
score = [0] * n
if n == 0:
    print(0)
    exit(0)
elif n == 1:
    print(l[0])
    exit(0)
elif n == 2:
    print(l[0] + l[1])
    exit(0)
score[0] = l[0]
score[1] = l[0] + l[1]
score[2] = max(l[0] + l[2], l[1] + l[2])

for i in range(3, n):
    score[i] = max(score[i-2], score[i-3] + l[i-1]) + l[i]
result = score[n-1]
print(result)