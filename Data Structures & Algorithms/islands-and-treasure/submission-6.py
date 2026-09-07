class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row not in range(rows) or
                        col not in range(cols) or
                        (row, col) in visited or
                        grid[row][col] == -1):
                        continue
                    
                    grid[row][col] = dist
                    visited.add((row, col))
                    q.append((row, col))
        



        