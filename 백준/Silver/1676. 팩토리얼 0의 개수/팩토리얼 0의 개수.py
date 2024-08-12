import sys
input = sys.stdin.readline

n = int(input())
f = 1
if n <= 0:
    print(0)
    exit(0)

for i in range(1, n+1):
    f *= i

cnt = 0
for i in range(1, n+1):
    if str(f)[-i] == '0':
        cnt += 1
    else:
        break
print(cnt)