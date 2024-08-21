import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = {input().rstrip() for _ in range(n)}
s = {input().rstrip() for _ in range(m)}
inter = list(l & s)
inter.sort()
print(len(inter))
for name in inter:
    print(name)