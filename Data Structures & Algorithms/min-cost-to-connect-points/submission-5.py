class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[(x1, y1)].append((dist, x2, y2))
                adj[(x2, y2)].append((dist, x1, y1))
        
        x, y = points[0]
        minHeap = [(0, x, y)]
        visited = set()
        res = 0


        while minHeap and len(visited) < len(points):
            cost, x, y = heapq.heappop(minHeap)

            if (x, y) in visited:
                continue

            res += cost
            visited.add((x, y))

            for dist, nei_x, nei_y in adj[(x, y)]:
                if (nei_x, nei_y) not in visited:
                    heapq.heappush(minHeap, (dist, nei_x, nei_y))
            
        
        return res