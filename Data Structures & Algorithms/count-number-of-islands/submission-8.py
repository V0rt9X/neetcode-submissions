class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                grid[r][c] == '0'):
                return
            
            grid[r][c] = '0'
            visited.add((r, c))

            for dr, dc in directions:
                dfs(dr + r, dc + c)
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands