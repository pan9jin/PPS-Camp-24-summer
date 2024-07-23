import sys
input = sys.stdin.readline
n, conn = int(input()), int(input())
g = [[] for i in range(n+1)]
visited = [0] * (n+1)
for _ in range(conn):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]
def DFS(v):
    visited[v] = 1
    for i in g[v]:
        if visited[i] == 0:
            DFS(i)
DFS(1)
print(sum(visited) - 1)