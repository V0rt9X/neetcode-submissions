class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1:
                return t
            
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (row not in range(rows) or
                    col not in range(cols) or
                    (row, col) in visited):
                    continue
                
                visited.add((row, col))
                heapq.heappush(minHeap, (max(grid[row][col], t), row, col))