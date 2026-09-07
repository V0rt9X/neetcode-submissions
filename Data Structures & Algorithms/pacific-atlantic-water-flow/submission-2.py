class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def addCell(r, c, visited, prevH):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                heights[r][c] < prevH):
                return
            
            visited.add((r, c))

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in directions:
                row, col = r + dr, c + dc

                addCell(row, col, visited, heights[r][c])
        
        for c in range(cols):
            addCell(0, c, pac, heights[0][c])
            addCell(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            addCell(r, 0, pac, heights[r][0])
            addCell(r, cols - 1, atl, heights[r][cols - 1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res