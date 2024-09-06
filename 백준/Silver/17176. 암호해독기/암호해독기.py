import sys
input = sys.stdin.readline

n = int(input())
crypt = list(map(int, input().split()))
origin = list(input().rstrip())
crypt.sort()
origin.sort()
for i in range(n):
    if crypt[i] == 0:
        crypt[i] = ' '
    elif crypt[i] <= 26:
        crypt[i] = chr(crypt[i]+64)
    else:
        crypt[i] = chr(crypt[i]+70)
if crypt == origin:
    print('y')
else:
    print('n')