import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def BFS(n, edges):
    g = [[] for _ in range(n+1)]
    for edge in edges:
        a, b = edge
        g[a].append(b)
        g[b].append(a)
    parent = [0] * (n+1)
    parent[1] = -1

    q = deque([1])
    while q:
        node = q.popleft()
        for neigh in g[node]:
            if parent[neigh] == 0:
                parent[neigh] = node
                q.append(neigh)
    return parent

edges = []
idx = 1
for _ in range(n-1):
    a, b = map(int, input().split())
    edges.append((a, b))
    idx += 2
parent = BFS(n, edges)

for i in range(2, n+1):
    print(parent[i])