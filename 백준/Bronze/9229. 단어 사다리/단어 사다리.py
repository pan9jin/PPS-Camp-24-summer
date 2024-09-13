import sys
input = sys.stdin.readline

word = list(input())
result = True
while True:
    prev_word = word
    word = list(input())
    if word[0] == '#':
        if prev_word[0] == '#':
            break
        else:
            print('Correct' if result else 'Incorrect')
            result = True
            continue
    if prev_word[0] == '#':
        continue
    if len(word) != len(prev_word):
        result = False
        continue
    cnt = 0
    for i in range(len(word)):
        if word[i] != prev_word[i]:
            cnt+=1
    if cnt != 1:
        result = False