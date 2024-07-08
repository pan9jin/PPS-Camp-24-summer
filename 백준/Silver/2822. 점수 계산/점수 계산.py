score = [int(input()) for _ in range(8)]
s_score = sorted(score, reverse=True)
result = []
for i in range(5):
    result.append(str(score.index(s_score[i])+1))
print(sum(n for n in s_score[:5]))
print(' '.join(sorted(result)))