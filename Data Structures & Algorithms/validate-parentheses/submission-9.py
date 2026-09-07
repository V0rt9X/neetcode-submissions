class Solution:
    def isValid(self, s: str) -> bool:
        rule = {')': '(', ']': '[', '}': '{'}
        stack = []

        for p in s:
            if p in rule:
                if stack and rule[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return not stack
