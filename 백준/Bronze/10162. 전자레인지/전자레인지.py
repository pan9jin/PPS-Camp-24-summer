import sys
input = sys.stdin.readline

t = int(input())
button = [300, 60, 10]
cnt = [0]*3

for i in range(3):
    cnt[i] = t // button[i]
    t %= button[i]

if t != 0:
    print(-1)
else:
    print(*cnt)
