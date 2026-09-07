class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        res = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                dimension = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                r, c = q.popleft()

                for dr, dc in dimension:
                    row, col = dr + r, dc + c
                    if (row in range(rows) and
                        col in range(cols) and
                        (row, col) not in visited and
                        grid[row][col] == '1'):
                        visited.add((row, col))
                        q.append((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        
        return res