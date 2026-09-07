class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((w, j))
                adj[j].append((w, i))
        
        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while len(visited) < n:
            w1, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            
            visited.add(src)
            res += w1

            for w2, dst in adj[src]:
                if dst not in visited:
                    heapq.heappush(minHeap, (w2, dst))
        
        return res