class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dst, cost in times:
            adj[src].append((cost, dst))
        
        res = 0
        minHeap = [(0, k)]
        visited = set()

        while minHeap:
            cost1, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            
            visited.add(src)
            
            res = max(res, cost1)

            for cost2, dst in adj[src]:
                if dst not in visited:
                    heapq.heappush(minHeap, (cost1 + cost2, dst))
        
        return res if len(visited) == n else -1