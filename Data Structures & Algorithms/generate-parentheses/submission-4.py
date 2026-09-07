class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openP, closeP, subS):
            if openP == closeP == n:
                res.append("".join(subS))
                return
            
            if openP < n:
                subS.append('(')
                backtrack(openP + 1, closeP, subS)
                subS.pop()
            
            if closeP < openP:
                subS.append(')')
                backtrack(openP, closeP + 1, subS)
                subS.pop()
        
        backtrack(0, 0, [])
        return res
