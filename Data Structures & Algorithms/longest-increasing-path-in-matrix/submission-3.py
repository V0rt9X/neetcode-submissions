class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if (r not in range(rows) or
                c not in range(cols) or
                matrix[r][c] <= prev):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            
            dp[(r, c)] = res
            return dp[(r, c)]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        
        return max(dp.values())
