import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    result = 1
    one = 1
    while True:
        if one % n == 0:
            print(result)
            break
        else:
            one = one*10 + 1
            result += 1