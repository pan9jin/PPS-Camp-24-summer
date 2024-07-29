import sys
input = sys.stdin.readline

n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    tmp = 0
    while n > 0:
        n -= 3
        tmp += 1
        if n % 5 == 0:
            tmp += n // 5
            print(tmp)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(tmp)
            break