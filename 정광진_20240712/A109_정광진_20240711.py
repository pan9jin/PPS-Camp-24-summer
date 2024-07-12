from fractions import Fraction

n = int(input())
d = 0
r = Fraction(1)
for _ in range(n):
    f, s, bd = map(int, input().split())
    d = (d + bd) % 2
    r *= Fraction(s, f)
print(d, int(float(r)))