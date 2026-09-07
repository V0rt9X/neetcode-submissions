class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != 1 or
                (r, c) in visited):
                return 0
            
            visited.add((r, c))
            res = 1
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea