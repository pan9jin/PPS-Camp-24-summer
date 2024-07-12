import sys
n, m = map(int, sys.stdin.readline().split())
brand = []
for _ in range(m):
    s_price, e_price = map(int, sys.stdin.readline().split())
    brand.append((s_price, e_price))
s_min = min(brand, key=lambda s: s[0])[0]
e_min = min(brand, key=lambda e: e[1])[1]
s_num = n // 6
remain = n - s_num*6
total = min(s_num*s_min + remain*e_min, (s_num+1)*s_min, n*e_min)
print(total)