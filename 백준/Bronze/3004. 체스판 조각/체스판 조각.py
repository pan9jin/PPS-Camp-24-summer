import sys
input = sys.stdin.readline

n = int(input())
if n %2 == 0:
    result = (n//2+1)**2
else:
    result = (n//2+1)*(n//2+2)
print(result)