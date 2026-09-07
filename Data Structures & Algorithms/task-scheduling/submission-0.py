class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        TaskCount = Counter(tasks)
        maxHeap = [-val for val in TaskCount.values()]
        heapq.heapify(maxHeap)

        q = collections.deque()
        cycle = 0

        while maxHeap or q:
            cycle += 1

            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    q.append((task, cycle + n))
            
            if q and q[0][1] == cycle:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return cycle
