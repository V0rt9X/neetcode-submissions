class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        visited = set()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        time = 0
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row not in range(rows) or
                        col not in range(cols) or
                        (row, col) in visited or
                        grid[row][col] == 0):
                        continue
                    
                    grid[row][col] = 2
                    fresh -= 1
                    visited.add((row, col))
                    q.append((row, col))
            

        return time if fresh == 0 else -1  