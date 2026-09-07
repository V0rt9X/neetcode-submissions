class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == '+':
                stack.append(stack.pop() + stack.pop())
            elif n == '-':
                b,a = stack.pop(),stack.pop()
                stack.append(a - b)
            elif n == '*':
                stack.append(stack.pop() * stack.pop())
            elif n == '/':
                b,a = stack.pop(),stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(n))
        
        return stack[-1]