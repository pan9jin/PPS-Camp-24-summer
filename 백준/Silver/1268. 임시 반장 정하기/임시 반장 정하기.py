import sys
input = sys.stdin.readline

n = int(input())
c = []
dup = [0] * n
for i in range(n):
    c.append(list(map(int, input().split())))
    dup[i] = [0] * n
for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if c[j][i] == c[k][i]:
                dup[k][j] = 1
                dup[j][k] = 1
answer = []
for i in dup:
    answer.append(i.count(1))
print(answer.index(max(answer))+1)