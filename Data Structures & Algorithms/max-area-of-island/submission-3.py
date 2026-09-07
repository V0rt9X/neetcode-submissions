class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                grid[r][c] != 1):
                return 0
            
            visited.add((r, c))

            area = 1
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                area += dfs(row, col)
            
            return area
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea