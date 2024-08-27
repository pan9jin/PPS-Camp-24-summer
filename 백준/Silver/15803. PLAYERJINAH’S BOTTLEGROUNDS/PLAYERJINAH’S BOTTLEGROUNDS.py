import sys
input = sys.stdin.readline

p = [list(map(int, input().split())) for _ in range(3)]

result = p[0][0]*p[1][1] + p[1][0]*p[2][1] + p[2][0]*p[0][1]
result -= (p[0][1]*p[1][0] + p[1][1]*p[2][0] + p[2][1]*p[0][0])

if result == 0:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")