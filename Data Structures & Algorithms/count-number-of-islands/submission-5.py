class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        def bfs(r, c):
            visited.add((r, c))
            q.append((r, c))

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        row, col = dr + r, dc + c

                        if (row not in range(rows) or
                            col not in range(cols) or
                            grid[row][col] == '0' or
                            (row, col) in visited):
                            continue
                        
                        visited.add((row, col))
                        q.append((row, col))
        
        island = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    island += 1
                    bfs(r, c)
        
        return island