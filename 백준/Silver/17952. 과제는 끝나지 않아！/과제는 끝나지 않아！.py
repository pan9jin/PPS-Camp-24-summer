import sys
input = sys.stdin.readline

n = int(input())
hw = []
score = 0
for _ in range(n):
    l = list(map(int, input().split()))
    if l[0] == 1:
        if l[2] == 1:
            score += l[1]
        else:
            hw.append([l[1], l[2]-1])
    else:
        if hw:
            hw[-1][1] -= 1
            if hw[-1][1] == 0:
                s, _ = hw.pop()
                score += s
print(score)        