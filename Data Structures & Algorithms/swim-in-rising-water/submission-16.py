class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        res = 0

        while minHeap:
            h, r, c = heapq.heappop(minHeap)

            res = max(res, h)

            if (r, c) == (rows - 1, cols - 1):
                return res

            if (r, c) in visited:
                continue
            
            
            visited.add((r, c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (row not in range(rows) or
                    col not in range(cols) or
                    (row, col) in visited):
                    continue
                heapq.heappush(minHeap, (grid[row][col], row, col))
        
        return res
