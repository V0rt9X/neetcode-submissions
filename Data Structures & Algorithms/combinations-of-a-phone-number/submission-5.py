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

        def backtrack(i, subC):
            if len(subC) == len(digits):
                res.append(subC)
                return
            
            for c in digitsToCh[digits[i]]:
                backtrack(i + 1, subC + c)
        
        if not digits:
            return []

        backtrack(0, "")
        return res