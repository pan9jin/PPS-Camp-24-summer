word = input()
t_sum = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for c in word:
    t_sum += 2
    for idx, group in enumerate(dial):
        if c in group:
            t_sum += idx + 1
print(t_sum)