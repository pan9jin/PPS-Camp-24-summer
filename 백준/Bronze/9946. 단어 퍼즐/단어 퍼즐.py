import sys
input = sys.stdin.readline

num = 0
while True:
    f = input().rstrip()
    s = input().rstrip()
    
    if f == 'END' and s == 'END':
        break
    
    num += 1
    first = {chr(i):0 for i in range(97, 123)}
    second = {chr(i):0 for i in range(97, 123)}
    for c in f:
        first[c] += 1
    for c in s:
        second[c] += 1
    
    if first == second:
        print(f'Case {num}: same')
    else:
        print(f'Case {num}: different')