class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while minHeap:
            dist, i = heapq.heappop(minHeap)

            if i in visited:
                continue
            
            res += dist
            visited.add(i)

            for nei_dist, nei_i in adj[i]:
                if nei_i not in visited:
                    heapq.heappush(minHeap, (nei_dist, nei_i))
        
        return res