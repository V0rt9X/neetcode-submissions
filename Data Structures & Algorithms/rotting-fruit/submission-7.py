class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        fresh = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        minute = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row not in range(rows) or
                        col not in range(cols) or
                        (row, col) in visited or
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))
                    visited.add((row, col))
            minute += 1
        
        return minute if fresh == 0 else -1