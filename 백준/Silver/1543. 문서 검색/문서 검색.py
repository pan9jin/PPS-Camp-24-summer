import sys
input = sys.stdin.readline
doc = input().strip()
search = input().strip()
s_len = len(search)
idx, cnt = 0, 0
while idx < len(doc):
    if doc[idx:idx+s_len] == search:
        cnt += 1
        idx += s_len
    else:
        idx += 1
print(cnt)