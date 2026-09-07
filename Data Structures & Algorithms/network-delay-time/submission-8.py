class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {node: [] for node in range(n + 1)}

        for src, dst, t in times:
            adj[src].append((t, dst))
        
        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            cost, src = heapq.heappop(minHeap)

            if src in visited:
                continue

            res = cost

            visited.add(src)

            for t, dst in adj[src]:
                if dst not in visited:
                    heapq.heappush(minHeap, (t + cost, dst))
        
        
        return res if len(visited) == n else -1