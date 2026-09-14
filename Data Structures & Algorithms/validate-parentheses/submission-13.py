class Solution:
    def isValid(self, s: str) -> bool:
        rule = {')': '(',
                ']': '[',
                '}': '{'}
            
        stack = []

        for c in s:
            if stack and c in rule:
                if rule[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return not stack