class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                grid[r][c] != '1'):
                return 0
            
            visited.add((r, c))

            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)
            
            return 1
        
        island = 0
        for r in range(rows):
            for c in range(cols):
                island += dfs(r, c)
        
        return island