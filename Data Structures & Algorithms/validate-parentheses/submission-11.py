class Solution:
    def isValid(self, s: str) -> bool:
        rules = {')': '(',
                 ']': '[',
                 '}': '{'}
        stack = []

        for c in s:
            if c in rules:
                if not stack or stack[-1] != rules[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return not stack
