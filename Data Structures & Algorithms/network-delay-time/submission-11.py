class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {src: [] for src in range(n + 1)}

        for src, dst, time in times:
            adj[src].append((time, dst))
        
        visited = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap:
            t_s, s = heapq.heappop(minHeap)
            
            if s in visited:
                continue
            
            res = max(res, t_s)
            visited.add(s)
            for t_d, d in adj[s]:
                heapq.heappush(minHeap, (t_d + t_s, d))
        
        return res if len(visited) == n else -1

        # T: O(e log v), S: O(v + e)