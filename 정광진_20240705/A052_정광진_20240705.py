n = int(input())
result = []
for _ in range(n):
    quiz = input()
    score = 0
    stack = 0
    for c in quiz:
        if c == 'O':
            stack += 1
            score += stack
        else:
            stack = 0
    result.append(score)
for score in result:
    print(score)