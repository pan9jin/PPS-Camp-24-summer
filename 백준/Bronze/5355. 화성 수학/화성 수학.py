t = int(input())
l = []
for _ in range(t):
    line = input().split()
    num = float(line[0])
    for op in line[1:]:
        if op == '@':
            num *= 3
        elif op == '%':
            num +=5
        elif op == '#':
            num -= 7
    l.append(round(num, 2))

for n in l:
    print("%.2f" % n)