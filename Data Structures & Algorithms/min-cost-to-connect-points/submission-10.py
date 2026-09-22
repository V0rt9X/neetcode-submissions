class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points) - 1):
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
            for dist_nei, i_nei in adj[i]:
                heapq.heappush(minHeap, (dist_nei, i_nei))
        
        return res

        # T: O(n log n) S: O(n)
