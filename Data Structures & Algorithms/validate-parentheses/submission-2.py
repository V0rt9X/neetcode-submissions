class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        toClose = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in toClose:
                if stack and stack[-1] == toClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack    