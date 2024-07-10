from collections import deque
n = int(input())
result = []
for _ in range(n):
    s = list(input())
    s_str = ''.join(s)
    s_cnt = 0
    for c in s:
        if c.isdigit():
            s_cnt+=int(c)
    result.append((s_str, s_cnt))

result.sort(key=lambda item: (len(item[0]), item[1], item[0]))

for item in result:
    print(item[0])