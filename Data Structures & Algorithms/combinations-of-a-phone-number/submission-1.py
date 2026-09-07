class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToCh = {'2': "abc",
                      '3': "def",
                      '4': "ghi",
                      '5': "jkl",
                      '6': "mno",
                      '7': "pqrs",
                      '8': "tuv",
                      '9': "wxyz"}
        
        res = []

        def backtrack(i, part):
            if len(part) == len(digits):
                res.append(part)
                return
            
            for c in digitsToCh[digits[i]]:
                backtrack(i + 1, part + c)

        if digits:
            backtrack(0, "")
            
        return res