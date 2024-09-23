import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pw = {}
for _ in range(n):
    note = list(input().split())
    pw[note[0]] = note[1]
result = []
for _ in range(m):
    site = input().rstrip()
    result.append(pw[site])
for s in result:
    print(s)