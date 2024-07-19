import sys
input = sys.stdin.readline
n, m = map(int, input().split())
poketmon = {}
for i in range(1, n+1):
    poketmon[i] = input().rstrip()
p_name = {v: k for k, v in poketmon.items()}
for _ in range(m):
    problem = input().rstrip()
    if problem.isdigit():
        print(poketmon[int(problem)])
    else:
        print(p_name[problem])