import sys
input = sys.stdin.readline

g1 = list(input().rstrip())
g2 = list(input().rstrip())

g1 = [int(g) - 1 for g in g1]
g2 = [int(g) - 1 for g in g2]

if len(g1) < len(g2):
    g1, g2 = g2, g1

result = float('inf')
for i in range(len(g1)):
    isAnd = False
    for j in range(i, min(len(g1), len(g2)+i)):
        if g1[j] & g2[j-i]:
            isAnd = True
            break
    if not isAnd:
        result = min(result, max(len(g1), len(g2)+i))

for i in range(len(g2)):
    isAnd = False
    for j in range(i, min(len(g1)+i, len(g2))):
        if g1[j-i] & g2[j]:
            isAnd = True
            break
    if not isAnd:
        result = min(result, max(len(g1)+i, len(g2)))
        
print(result if result != float('inf') else len(g1)+len(g2))