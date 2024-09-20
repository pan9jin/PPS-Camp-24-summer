import sys
input = sys.stdin.readline

k, l = map(int, input().split())
s = list(input().rstrip())

for i in range(l):
    if ord('A') <= ord(s[i]) <= ord('Z'):
        s[i] = chr(ord('A')+(ord(s[i]) - ord('A') + k)  % 26)
    if ord('a') <= ord(s[i]) <= ord('z'):
        s[i] = chr(ord('a')+(ord(s[i]) - ord('a') + k)  % 26)
    print(s[i], end='')
print('')