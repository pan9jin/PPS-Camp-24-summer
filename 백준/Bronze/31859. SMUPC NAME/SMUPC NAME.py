import sys
input = sys.stdin.readline

n, s = input().split()
result = ""
cnt = 0
for i in s:
    if i not in result:
        result += i
    else:
        cnt += 1
result = str(int(n)+1906) + result + str(cnt + 4)
print('smupc_'+result[::-1])