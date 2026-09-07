class Solution:
    def isValid(self, s: str) -> bool:
        rule = {']': '[', '}': '{', ')': '('}
        stack = []

        for c in s:
            if c in rule:
                if stack and rule[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack