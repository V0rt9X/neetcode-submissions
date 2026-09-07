class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # List to store and validate seen brackets
        toClose = {')':'(',']':'[','}':'{'} # Rule for validating

        for c in s:
            if c in toClose: #Validation if c(char) is open bracket
                if stack and stack[-1] == toClose[c]: # Validation if stack exsist elements and if last element is the oposite bracket to c (char)
                    stack.pop() 
                else:
                    return False
            else: # appending value if it isn't in toClose which mean all open brackets
                stack.append(c) 
        
        return True if not stack else False 