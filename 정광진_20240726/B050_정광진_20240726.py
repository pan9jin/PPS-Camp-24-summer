import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
g = [[] for _ in range(v+1)]

for _ in range(v):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        adj = data[idx]
        w = data[idx + 1]
        g[node].append((adj, w))
        idx += 2

def BFS(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (v+1)
    visited[start] = 0
    res = [0, 0]

    while q:
        node, node_w = q.popleft()
        for adj, adj_w in g[node]:
            if visited[adj] == -1:
                d = node_w + adj_w
                q.append((adj, d))
                visited[adj] = d
                if res[1] < d:
                    res[0] = adj
                    res[1] = d
    return res

point, _ = BFS(1)
print(BFS(point)[1])