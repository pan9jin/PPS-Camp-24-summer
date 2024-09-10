import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

friend = [[0 for _ in range(n+1)] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a][b] = 1
    friend[b][a] = 1


for i in range(1, n+1):
    q = deque([[i, 0]])
    visited = [False for _ in range(n+1)]
    num = 0
    while q:
        v, d = q.popleft()
        num += d
        
        visited[v] = True

        for j in range(1, len(friend[v])):
            if friend[v][j] == 1 and visited[j] == False:
                visited[j] = True
                q.append([j, d+1])            
                
    result[i] = num

min_num = 99999
result_num = -1

for i in range(1, n+1):
    if result[i] < min_num:
        min_num = result[i]
        result_num = i
        
print(result_num)