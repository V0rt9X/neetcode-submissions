class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0

            res = 1
            for dr, dc in directions:
                row, col = dr + r, dc + c
                res += dfs(row, col)
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res

        
