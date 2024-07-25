import sys
input = sys.stdin.readline

exp = input()
sub_exp = exp.split('-')
answer = sum(map(int, sub_exp[0].split('+')))

for e in sub_exp[1:]:
    answer -= sum(map(int, e.split('+')))

print(answer)