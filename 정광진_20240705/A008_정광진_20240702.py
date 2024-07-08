num = int(input())
result = []

for _ in range(num):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    up = sum(1 for s in score[1:] if s > avg)
    result.append(up / score[0] * 100)

for res in result:
    print(f"{res:.3f}%")
