import sys
input = sys.stdin.readline
s = input().rstrip()
s1 = s.split('0')
s2 = s.split('1')
a = len(s1) - s1.count('')
b = len(s2) - s2.count('')
print(min(a, b))