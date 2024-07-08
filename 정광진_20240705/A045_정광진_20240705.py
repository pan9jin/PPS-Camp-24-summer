s = input().upper()
f = {}
for c in s:
    if c in f:
        f[c] += 1
    else:
        f[c] = 1
tmp = [k for k, v in f.items() if max(f.values()) == v]
print(tmp[0] if len(tmp) == 1 else '?')