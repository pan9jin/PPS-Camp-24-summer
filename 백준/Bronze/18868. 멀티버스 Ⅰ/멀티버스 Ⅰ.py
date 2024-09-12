import sys
input = sys.stdin.readline

m, n = map(int, input().split())
space = []

for _ in range(m):
    space.append(list(map(int, input().split())))

def solve(p1, p2):
    for i in range(n):
        for j in range(i+1, n):
            if p1[i] == p1[j]:
                if p2[i] != p2[j]:
                    return False
            elif p1[i] > p1[j]:
                if p2[i] <= p2[j]:
                    return False
            elif p1[i] < p1[j]:
                if p2[i] >= p2[j]:
                    return False
    return True

cnt = 0
for i in range(m):
    for j in range(i+1, m):
        if solve(space[i], space[j]):
            cnt+=1
print(cnt)