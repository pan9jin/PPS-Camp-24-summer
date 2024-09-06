import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n *= 3
m *= 8
problem = [list(input().rstrip()) for _ in range(n)]

for i in range(0, n, 3):
    for j in range(0, m, 8):
        a, b, c = int(problem[i+1][j+1]), int(problem[i+1][j+3]), int(problem[i+1][j+5])
        if problem[i+1][j+6] != '.':
            c = c*10 + int(problem[i+1][j+6])
        if a+b == c:
            mark = 7 if c >= 10 else 6
            problem[i+1][j] = '*'
            problem[i+1][j+mark] = '*'
            for k in range(1, mark):
                problem[i][j+k] = '*'
                problem[i+2][j+k] = '*'
        else:
            for k in range(3):
                problem[i+k][j+3-k] = '/'

for p in problem:
    print(''.join(p))