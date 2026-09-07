class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        island = 0
        def Island(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                grid[r][c] == '0'):
                return
            
            visited.add((r, c))

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

            for dr, dc in directions:
                row, col = dr + r, dc + c
                Island(row, col)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    island += 1
                    Island(r, c)
        
        return island
