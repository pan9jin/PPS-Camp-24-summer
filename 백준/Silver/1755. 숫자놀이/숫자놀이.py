m, n = map(int, input().split())
char = ['zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']
r1 = []
for num in range(m, n+1):
    l = [char[int(c)] for c in str(num)]
    r1.append((' '.join(l), num))

r2 = [item[1] for item in sorted(r1, key=lambda a: a[0])]
for i in range(len(r2)):
    if (i+1) % 10 == 0 or i == len(r2) - 1:
        print(r2[i])
    else:
        print(r2[i], end=' ')