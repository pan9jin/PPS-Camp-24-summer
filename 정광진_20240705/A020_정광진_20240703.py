result = 0
s = 0
for _ in range(4):
    off, on = map(int, input().split())
    s-=off
    result = max(result, s)
    s+=on
    result = max(result, s)
print(result)