class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(matrix), len(matrix[0])

        dp = {}

        def dfs(r, c, prevVal):
            if (r not in range(rows) or
                c not in range(cols) or
                matrix[r][c] <= prevVal):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            for dr, dc in directions:
                res = max(1 + dfs(dr + r, dc + c, matrix[r][c]), res)
            dp[(r, c)] = res

            return res
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        
        return max(dp.values())
