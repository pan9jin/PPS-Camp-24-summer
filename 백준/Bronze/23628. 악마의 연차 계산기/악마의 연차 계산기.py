import sys
input = sys.stdin.readline

s = list(map(int, input().split()))
e = list(map(int, input().split()))
d = (e[0]-s[0])*360 + (e[1]-s[1])*30 + (e[2]-s[2])

m = min(d//30, 36)

a = 0
wy = 0
y = 0
years = d//360

for year in range(1, years+1):
    y += 15 + a
    wy += 1
    if wy == 2:
        a += 1
        wy = 0

print(y, m)
print(f'{d}days')