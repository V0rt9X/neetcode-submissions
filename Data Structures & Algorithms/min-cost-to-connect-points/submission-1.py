class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while len(visited) < n:
            dist, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            
            visited.add(src)
            res += dist

            for dist2, dst in adj[src]:
                if dst not in visited:
                    heapq.heappush(minHeap, (dist2, dst))
        
        return res