import sys, math
input = sys.stdin.readline

n, a, b = map(int, input().split())
lecture = [list(map(int, input().split())) for _ in range(10)]
if a >= 66 and b >= 130:
    print("Nice")
else:
    for i in range(8-n):
        a += lecture[i][0] * 3
        b += lecture[i][0] * 3
        l = 6 - lecture[i][0]
        if l < lecture[i][1]:
            b += l * 3
        else:
            b += lecture[i][1] * 3
    if a >= 66 and b >= 130:
        print("Nice")
    else:
        print("Nae ga wae")