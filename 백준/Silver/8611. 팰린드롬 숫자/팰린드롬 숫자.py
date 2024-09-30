import sys
input = sys.stdin.readline

n = int(input())

result = []
for k in range(2, 11):
    tmp = n
    pal = []
    while tmp > 0:
        d = tmp%k
        tmp //= k
        pal.append(str(d))
    if pal == pal[::-1]:
        result.append((k, ''.join(pal)))

if len(result) == 0:
    print("NIE")
else:
    for b, m in result:
        print(b, m)