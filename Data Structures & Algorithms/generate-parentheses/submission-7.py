class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openP, closeP, path):
            if openP == closeP == n:
                res.append("".join(path))
                return
            
            if openP < n:
                path.append('(')
                backtrack(openP + 1, closeP, path)
                path.pop()

            if closeP < openP:
                path.append(')')
                backtrack(openP, closeP + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res

        # T: O(B^D * W) - > O(2^n * n) S: O(D) - > O(n)