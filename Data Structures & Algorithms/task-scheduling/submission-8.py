class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.deque()
        counter = Counter(tasks)
        maxHeap = [-c for c in counter.values()]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                c = heapq.heappop(maxHeap)

                if c + 1 != 0:
                    q.append((time + n, c + 1))
            
            if q and q[0][0] == time:
                p, c = q.popleft()
                heapq.heappush(maxHeap, c)
            
        
        return time