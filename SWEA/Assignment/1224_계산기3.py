T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()

    icp = {'+':1, '-':1, '*':2, '/':2, '(':3}  # 스택 밖
    isp = {'+':1, '-':1, '*':2, '/':2, '(':0}  # 스택 안

    def get_postfix(infix, n):
        postfix = ""
        stack = []

        for i in range(n):
            # 1. 연산자 or 피연산자?
            if infix[i] not in '()+-*/':
                postfix += infix[i]
            elif infix[i] == '(':
                stack.append(infix[i])
            elif infix[i] == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()  
            else:  
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])
        while stack:
            postfix += stack.pop()
        return postfix

    def get_result(postfix):
        stack = []

        for c in postfix:
            if c not in '+-/*':  # 숫자
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(a - b)
                elif c == '*':
                    stack.append(a * b)
                elif c == '/':
                    stack.append(a // b)
        return stack.pop()

    postfix = get_postfix(infix, N)
    result = get_result(postfix)
    print(f'#{tc} {result}')