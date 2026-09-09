class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        time = 0
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()


                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row not in range(rows) or
                        col not in range(cols) or
                        (row, col)in visited or
                        grid[row][col] == -1):
                        continue
                    
                    grid[row][col] = time
                    q.append((row, col))
                    visited.add((row, col))
                    
