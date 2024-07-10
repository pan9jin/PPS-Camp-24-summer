l = list(input())
cnt = 0
i = 0
while i < len(l):
    if l[i] == 'c' and i + 1 < len(l) and l[i + 1] in ['=', '-']:
        cnt += 1
        i += 2
    elif l[i] == 'd' and i + 1 < len(l) and l[i + 1] == '-':
        cnt += 1
        i += 2
    elif l[i] == 'd' and i + 2 < len(l) and l[i + 1] == 'z' and l[i + 2] == '=':
        cnt += 1
        i += 3
    elif l[i] in ['l', 'n'] and i + 1 < len(l) and l[i + 1] == 'j':
        cnt += 1
        i += 2
    elif l[i] in ['s', 'z'] and i + 1 < len(l) and l[i + 1] == '=':
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1
print(cnt)