class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        combS = []
        def backtracking(openS, closeS):
            if openS == closeS == n:
                res.append("".join(combS))
                return
            
            if openS < n:
                combS.append('(')
                backtracking(openS + 1, closeS)
                combS.pop()
            
            if closeS < openS:
                combS.append(')')
                backtracking(openS, closeS + 1)
                combS.pop()
            
        backtracking(0, 0)
        return res