class Solution:
    def checkValidString(self, s: str) -> bool:

        leftM, rightM = 0, 0
        
        for c in s:
            if c == '(':
                leftM += 1
                rightM += 1
            elif c == ')':
                leftM -= 1
                rightM -= 1
            else:
                leftM -= 1
                rightM += 1
            
            if leftM < 0:
                leftM = 0
            if rightM < 0:
                return False
        
        return leftM == 0
