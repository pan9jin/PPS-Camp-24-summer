import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n)]
def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    conn = list(map(int, input().split()))
    for j in range(n):
        if conn[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
result = set(find(i-1) for i in plan)
            
print("YES" if len(result) == 1 else "NO")