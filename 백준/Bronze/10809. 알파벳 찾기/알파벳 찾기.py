import sys
input = sys.stdin.readline

s = input().strip()
s_list = list(s)
dic = {key:-1 for key in [chr(i) for i in range(97,123)]}
for c in s_list:
    if dic[c] == -1:
        dic[c] = s_list.index(c)
print(*dic.values())