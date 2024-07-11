n = int(input())
d = 0
r = 1
for _ in range(n):
    f, s, bd = map(int, input().split())
    d = d if bd == 0 else not d
    r *= (s / f)
print(int(d), int(r))