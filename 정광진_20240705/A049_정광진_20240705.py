words = []
while True:
    s = input()
    if s == 'end':
        break
    words.append(s)
result = [] * len(words)
for word in words:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    accept = any(c in vowels for c in word)    
    v_cnt = 0
    c_cnt = 0
    for c in word:
        if c in vowels:
            v_cnt += 1
            c_cnt = 0
        else:
            v_cnt = 0
            c_cnt += 1
        if v_cnt >= 3 or c_cnt >= 3:
            accept = False
            break
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            if word[i] not in {'e', 'o'}:
                accept = False
    result.append(accept)
for i in range(len(words)):
    print("<%s> is %sacceptable." % (words[i], '' if result[i] else 'not '))