class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                val1, val2 = stack.pop(), stack.pop()
                val1, val2 = val2, val1
                stack.append(val1 - val2)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                val1, val2 = stack.pop(), stack.pop()
                val1, val2 = val2, val1

                stack.append(int(val1 / val2))
            else:
                stack.append(int(c))
            
        

        return stack[-1]