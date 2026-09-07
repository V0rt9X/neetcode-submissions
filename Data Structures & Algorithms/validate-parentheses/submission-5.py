class Solution:
    def isValid(self, s: str) -> bool:
        key = {'}': '{', ']': '[',')': '('}
        stack = []

        for n in s:
            if n in key:
                if stack and stack[-1] == key[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        
        return not stack