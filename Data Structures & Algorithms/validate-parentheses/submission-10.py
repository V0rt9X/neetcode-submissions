class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rule = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in rule:
                if stack and stack[-1] == rule[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack