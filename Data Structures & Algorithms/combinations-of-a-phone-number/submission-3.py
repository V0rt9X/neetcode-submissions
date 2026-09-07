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

        def backtracking(i, subS):
            if len(subS) == len(digits):
                res.append("".join(subS))
                return
            
            for c in digitsToCh[digits[i]]:
                subS.append(c)
                backtracking(i + 1, subS)
                subS.pop()
        
        if digits:
            backtracking(0, [])
        return res
