class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visited, prevMax):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                heights[r][c] < prevMax):
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col, visited, heights[r][c])


        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)
        
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res