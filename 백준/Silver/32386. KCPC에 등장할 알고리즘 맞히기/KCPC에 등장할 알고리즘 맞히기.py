import sys
input = sys.stdin.readline

n = int(input())
p_dict = {}
for _ in range(n):
    p_in = list(input().split())
    p_list = p_in[2:]
    for p in p_list:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1
max_val = max(p_dict.values())
result = [k for k, v in p_dict.items() if v == max_val]
print(result[0] if len(result) == 1 else -1)