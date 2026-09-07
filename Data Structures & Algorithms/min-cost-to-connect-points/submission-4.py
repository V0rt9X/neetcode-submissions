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
        
        visited = set()
        x, y = points[0]
        minHeap = [(0, x, y)]
        res = 0

        while len(visited) < len(points):
            dist1, x1, y1 = heapq.heappop(minHeap)

            if (x1, y1) in visited:
                continue

            visited.add((x1, y1))
            res += dist1

            for dist2, x2, y2 in adj[(x1, y1)]:
                if (x2, y2) not in visited:
                    heapq.heappush(minHeap, (dist2, x2, y2))
        
        return res