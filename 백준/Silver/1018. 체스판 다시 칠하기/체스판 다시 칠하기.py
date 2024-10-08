import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
answer = []
for i in range(n-7):
    for j in range(m-7):
        d1 = 0
        d2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        d1 += 1
                    if board[a][b] != 'W':
                        d2 += 1
                else:
                    if board[a][b] != 'W':
                        d1 += 1
                    if board[a][b] != 'B':
                        d2 += 1
        answer.append(d1)
        answer.append(d2)

print(min(answer))