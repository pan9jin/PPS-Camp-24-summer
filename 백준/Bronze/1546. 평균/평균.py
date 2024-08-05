import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
m_score = max(score)
score = [s/m_score*100 for s in score]
print(sum(score)/n)