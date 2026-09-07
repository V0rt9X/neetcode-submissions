class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rule = {')': '(',']': '[','}': '{'}

        for el in s:
            if el in rule:
                if stack and stack[-1] == rule[el]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(el)
        
        return not stack