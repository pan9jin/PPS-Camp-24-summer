import sys
n = int(sys.stdin.readline().rstrip())
s = 1
for _ in range(n):
    s += int(sys.stdin.readline().rstrip()) - 1
print(s)