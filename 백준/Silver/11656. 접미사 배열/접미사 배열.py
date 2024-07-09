s = list(input())
result = []
for i in range(len(s)):
    result.append(''.join(s[i::]))

for i in range(len(result)):
    print(sorted(result)[i])