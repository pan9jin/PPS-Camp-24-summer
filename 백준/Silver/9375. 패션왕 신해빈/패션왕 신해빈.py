import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        c_name, c_type = input().split()
        if c_type in clothes:
            clothes[c_type] += 1
        else:
            clothes[c_type] = 1
    result = 1
    for v in clothes.values():
        result *= v+1
    print(result-1)