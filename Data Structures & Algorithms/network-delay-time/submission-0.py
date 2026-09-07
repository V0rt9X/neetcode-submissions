class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dst, t in times:
            adj[src].append((t, dst))
        
        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            t1, src = heapq.heappop(minHeap)

            if src in visited:
                continue
            
            visited.add(src)
            res = max(res, t1)

            for t2, dst in adj[src]:
                if not dst in visited:
                    heapq.heappush(minHeap, (t1 + t2, dst))
        
        return res if len(visited) == n else -1