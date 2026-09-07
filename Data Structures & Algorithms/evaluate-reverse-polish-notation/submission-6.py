class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
                
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                val1, val2 = stack.pop(), stack.pop()

                stack.append(int(val2 / val1))
            else:
                stack.append(int(c))
            
        

        return stack[-1]