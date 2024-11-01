import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n):
    a, b = map(int, input().split())
    line.append([a, b])
line.sort(key = lambda x: x[0])

lis = [[] for _ in range(n)]
for i in range(n):
    if i == 0:
        lis[i].append(line[i][1])
    else:
        for j in range(0, i):
            if lis[j][-1] < line[i][1]:
                if len(lis[i]) - 1 < len(lis[j]):
                    lis[i] = lis[j]+[line[i][1]]
        if not lis[i]:
            lis[i].append(line[i][1])

result = 0
for i in range(n):
    result = max(result, len(lis[i]))
print(n - result)