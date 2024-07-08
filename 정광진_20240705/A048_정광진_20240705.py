n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    already = set()
    last = ''
    flag = True
    for c in s:
        if c != last:
            if c in already:
                flag = False
            already.add(c)
            last = c
    if flag:
        cnt+=1
print(cnt)