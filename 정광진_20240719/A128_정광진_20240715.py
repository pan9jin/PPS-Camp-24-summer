while True:
    s = input()
    if s == '.':
        break 

    stack = []
    bal = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                bal = False 
                break 
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                bal = False
                break 

    if bal and not stack:
        print('yes')
    else:
        print('no')