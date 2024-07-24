import sys
input = sys.stdin.readline

t = int(input())
cnt = [0]*3
while t > 0:
    if t >= 300:
        t -= 300
        cnt[0] += 1
    elif t >= 60:
        t -= 60
        cnt[1] += 1
    elif t >= 10:
        t -= 10
        cnt[2] += 1
    else:
        print(-1)
        exit(0)
print(*cnt)