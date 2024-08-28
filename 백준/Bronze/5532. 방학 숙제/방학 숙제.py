import sys
input = sys.stdin.readline

l, a, b, c, d = int(input()), int(input()), int(input()), int(input()), int(input())
print(l - max(a//c + (a%c>0), b//d + (b%d>0)))