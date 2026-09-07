class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.deque()
        # count = Counter(tasks)
        maxHeap = [-taskC for taskC in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        cycle = 0
        while maxHeap or q:
            cycle += 1
            if maxHeap:
                taskC = heapq.heappop(maxHeap) + 1
                if taskC:
                    q.append((cycle + n, taskC))
            
            if q and q[0][0] == cycle:
                heapq.heappush(maxHeap, q.popleft()[1])
        
        return cycle
                

