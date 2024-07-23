import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
g = [[] for _ in range(n+1)]
dfs_result = []
bfs_result = []
for _ in range(m):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]

for i in range(1, n+1):
    g[i].sort()

def DFS(v):
    visited[v] = 1
    dfs_result.append(v)
    for i in g[v]:
        if visited[i] == 0:
            DFS(i)

def BFS(v):
    q = deque([v])
    visited[v] = 1
    while q:
        c = q.popleft()
        bfs_result.append(c)
        for i in g[c]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

visited = [0] * (n+1)
DFS(v)
visited = [0] * (n+1)
BFS(v)

print(*dfs_result)
print(*bfs_result)