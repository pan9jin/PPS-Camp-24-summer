import sys
input = sys.stdin.readline

n, s = input().split()
n = int(n)
l = []
for _ in range(n):
    nick, chat = input().split()
    if nick == s:
        answer = chat
    if not any(n == nick for n, _ in l):
        l.append((nick, chat))

cnt = 0
for nick, chat in l:
    if chat != answer:
        continue
    if nick == s:
        print(cnt)
        break
    else:
        cnt+=1