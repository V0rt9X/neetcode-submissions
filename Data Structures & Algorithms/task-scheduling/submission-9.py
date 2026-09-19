class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [(-c, t) for t, c in Counter(tasks).items()]
        q = collections.deque()
        heapq.heapify(maxHeap)

        cycle = 0
        while maxHeap or q:
            cycle += 1
            if maxHeap:
                c, t = heapq.heappop(maxHeap)
                if c + 1 != 0:
                    q.append((cycle + n, c + 1, t))
            
            if q and q[0][0] == cycle:
                _, c, t = q.popleft()
                heapq.heappush(maxHeap, (c, t))
        
        return cycle
