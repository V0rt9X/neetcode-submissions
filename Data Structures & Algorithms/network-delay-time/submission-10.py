class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {node: [] for node in range(n + 1)}

        for src, dst, t in times:
            adj[src].append((t, dst))
        
        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            t, src = heapq.heappop(minHeap)

            if src in visited:
                continue
            
            visited.add(src)
            res = t
            for dst_t, dst in adj[src]:
                if dst not in visited:
                    heapq.heappush(minHeap, (t + dst_t, dst))
        
        return res if len(visited) == n else -1