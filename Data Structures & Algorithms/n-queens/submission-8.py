class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for _ in range(n)]
        
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(grid[r]) for r in range(n)])
                return
            
            for c in range(n):
                if (c in cols or r + c in posDiag or r - c in negDiag):
                    continue
                
                grid[r][c] = 'Q'
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)

                grid[r][c] = '.'
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        
        backtrack(0)
        return res