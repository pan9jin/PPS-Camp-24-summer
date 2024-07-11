n = int(input())
result = []
for _ in range(n):
    num = list(input())
    reverse = int(''.join(num[::-1]))
    num = int(''.join(num))
    s = list(str(num+reverse))
    if s == list(reversed(s)):
        result.append('YES')
    else:
        result.append('NO')
for r in result:
    print(r)