import sys
input = sys.stdin.readline

n = int(input())
word = [input().strip() for _ in range(n)]
word = list(set(word))
word.sort()
word.sort(key=lambda a: len(a))
for w in word:
    print(w)