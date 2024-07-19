import sys
input = sys.stdin.readline
n1, n2 = int(input()), list(input())
num2 = int(''.join(n2))
print(n1 * int(n2[2]))
print(n1 * int(n2[1]))
print(n1 * int(n2[0]))
print(n1 * num2)