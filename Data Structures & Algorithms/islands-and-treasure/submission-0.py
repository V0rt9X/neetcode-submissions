class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()

        def addGrid(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or
                (r, c) in visited or grid[r][c] == -1):
                return
            
            visited.add((r, c))
            q.append((r, c))
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = distance
                
                addGrid(r + 1, c)
                addGrid(r - 1, c)
                addGrid(r, c + 1)
                addGrid(r, c - 1)
            distance += 1
        
