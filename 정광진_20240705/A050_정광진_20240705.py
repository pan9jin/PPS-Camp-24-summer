word = input()
trans = []
for c in word:
    if c in {'A', 'B', 'C'}:
        trans.append(chr(ord(c) + 23))
    else:
        trans.append(chr(ord(c) - 3))
print(''.join(trans))