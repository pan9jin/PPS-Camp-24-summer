import sys
input = sys.stdin.readline

n = int(input())
if n < 3:
    print(4)
else:
    for i in range(2, n):
        if n <= i*i:
            print((i-1)*4)
            break
        elif n <= i*(i+1):
            print((i-1)*4+2)
            break