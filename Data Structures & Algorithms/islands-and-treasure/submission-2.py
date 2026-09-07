class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                if (r not in range(rows) or
                    c not in range(cols) or
                    (r, c) in visited or
                    grid[r][c] == -1):
                    continue
                
                grid[r][c] = dist
                visited.add((r, c))

                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    q.append((row, col))
            dist += 1