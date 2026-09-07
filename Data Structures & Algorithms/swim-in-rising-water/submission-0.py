class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1:
                return t
            
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c

                if (nei_r not in range(rows) or 
                    nei_c not in range(cols) or
                    (nei_r, nei_c) in visited):
                    continue

                visited.add((nei_r, nei_c))
                heapq.heappush(minHeap, (max(t, grid[nei_r][nei_c]), nei_r, nei_c))          