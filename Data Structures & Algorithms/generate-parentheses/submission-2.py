class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        subStr = []
        def backtrack(Ocount, Ccount):
            if Ocount == Ccount == n:
                res.append("".join(subStr))
                return
            
            if Ocount < n:
                subStr.append('(')
                backtrack(Ocount + 1, Ccount)
                subStr.pop()
            
            if Ccount < Ocount:
                subStr.append(')')
                backtrack(Ocount, Ccount + 1)
                subStr.pop()
            
        backtrack(0,0)
        return res