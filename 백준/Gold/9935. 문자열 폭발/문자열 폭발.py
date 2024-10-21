import sys

input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

stack = []
last = len(bomb) - 1

for char in string:
    stack.append(char)
    if char == bomb[last] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

result = ''.join(stack)
print(result if result else "FRULA")