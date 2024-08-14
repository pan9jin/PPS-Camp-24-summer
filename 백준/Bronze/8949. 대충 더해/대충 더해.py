import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
if len(a) > len(b):
    b = b.zfill(len(a))
else:
    a = a.zfill(len(b))
a, b = list(a), list(b)
result = ''
for i in range(len(a)):
    result += str(int(a[i])+int(b[i]))

print(result)