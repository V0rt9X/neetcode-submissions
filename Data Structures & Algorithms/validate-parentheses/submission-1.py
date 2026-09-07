class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # List to store and validate brackets
        toClose = {')': '(', ']': '[', '}' : '{'} # Rule for validating

        for c in s:
            if c in toClose: # Logic of validation brackets
                if stack and stack[-1] == toClose[c]: # Validation if bracket is 'close'
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)    
        
        return not stack