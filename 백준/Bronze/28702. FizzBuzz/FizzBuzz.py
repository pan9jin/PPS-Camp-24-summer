import sys
input = sys.stdin.readline

for i in range(3, 0, -1):
    a = input().rstrip()
    if a not in ['FizzBuzz', 'Fizz', 'Buzz']:
        n = int(a) + i

if n%15 == 0:
    print('FizzBuzz')
elif n%3 == 0:
    print('Fizz')
elif n%5 == 0:
    print('Buzz')
else:
    print(n)