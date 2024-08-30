import sys
input = sys.stdin.readline

p, w = map(int, input().split())
msg = input().rstrip()
time = 0
button = [[], [' '], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
past_num = 0
for c in msg:
    for i in range(len(button)):
        if c in button[i]:
            if c == ' ':
                time += p
                past_num = i
            else:
                for j in range(len(button[i])):
                    if c == button[i][j]:
                        if past_num == i:
                            time += (p*(j+1)+w)
                        else:
                            past_num = i
                            time += p*(j+1)
print(time)