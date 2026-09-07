class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row not in range(rows) or col not in range(cols) or
                        grid[row][col] == -1 or (row, col) in visited):
                        continue
                    
                    grid[row][col] = dist
                    q.append((row, col))
                    visited.add((row, col))
