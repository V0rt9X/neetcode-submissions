class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == '0'):
                return
            
            grid[r][c] = '0'
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)
        
        isLand = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    isLand += 1
                    dfs(r, c)

        return isLand