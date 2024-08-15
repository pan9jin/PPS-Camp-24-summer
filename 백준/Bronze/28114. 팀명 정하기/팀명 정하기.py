import sys
input = sys.stdin.readline

year = []
l = []
for _ in range(3):
    p, y, n = input().split()
    year.append(int(y)%100)
    l.append([int(p), n[0]])

year.sort()
year = list(map(str, year))
l.sort(key=lambda v:v[0], reverse=True)
l = [n[1] for n in l]
print(''.join(year))
print(''.join(l))