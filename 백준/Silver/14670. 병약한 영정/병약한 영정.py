import sys
input = sys.stdin.readline

n = int(input())
medicine = {}
for _ in range(n):
    effect, name = map(int, input().split())
    medicine[effect] = name

r = int(input())
for _ in range(r):
    rin = list(map(int, input().split()))
    result = []
    for s in rin[1:]:
        if s in medicine:
            result.append(medicine[s])
        else:
            print("YOU DIED")
            break
    else:
        print(*result)