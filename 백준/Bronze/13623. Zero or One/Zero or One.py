import sys
input = sys.stdin.readline

a, b, c = input().strip().split()
if a == b == c:
    print('*')
elif a == b:
    print('C')
elif b == c:
    print('A')
elif a == c:
    print('B')