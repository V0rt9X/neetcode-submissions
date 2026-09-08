class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                adj[i].append((abs(x1 - x2) + abs(y1 - y2), j))
                adj[j].append((abs(x1 - x2) + abs(y1 - y2), i))
        
        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while minHeap:
            dist, i = heapq.heappop(minHeap)

            if i in visited:
                continue
            
            visited.add(i)
            
            res += dist
            for nei_dist, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, (nei_dist, nei))
        
        return res


                
