import sys
input = sys.stdin.readline

n, k = int(input()), list(map(int, input().rstrip()))
even, odd = 0, 0
for c in k:
    if c%2 == 0 or c == 0:
        even+=1
    else:
        odd+=1
if even > odd:
    print(0)
elif odd > even:
    print(1)
else:
    print(-1)