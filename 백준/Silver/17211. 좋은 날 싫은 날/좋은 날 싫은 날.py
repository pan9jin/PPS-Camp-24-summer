n, curr = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

good = [0] * (n+1)
bad = [0] * (n+1)
good[0] = 1 if curr == 0 else 0
bad[0] = 1 if curr == 1 else 0

for day in range(1, n + 1):
    if day == 1:
        good[1] = good[0] * gg + bad[0] * bg
        bad[1] = good[0] * gb + bad[0] * bb
    else:
        good[day] = good[day - 1] * gg + bad[day - 1] * bg
        bad[day] = good[day - 1] * gb + bad[day - 1] * bb

print(round(good[n] * 1000))
print(round(bad[n] * 1000))