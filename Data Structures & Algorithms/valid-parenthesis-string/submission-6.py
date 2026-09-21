class Solution:
    def checkValidString(self, s: str) -> bool:
        minO, maxO = 0, 0

        for c in s:
            if c == '(':
                minO += 1
                maxO += 1
            elif c == ')':
                minO -= 1
                maxO -= 1
            else:
                minO -= 1
                maxO += 1
            
            if minO < 0:
                minO = 0
            if maxO < 0:
                return False
        
        return True if minO == 0 else False

        # T: O(n), S: O(1)
