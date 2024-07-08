n = int(input())
l = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x, y))

output = sorted(l, key=lambda point:(point[0], point[1]))

for p in output:
    print(p[0], p[1])