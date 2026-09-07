class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)

        q = collections.deque()
        cycle = 0

        while maxHeap or q:
            cycle += 1

            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    q.append([cycle + n, task])
            
            if q and q[0][0] == cycle:
                heapq.heappush(maxHeap, q.popleft()[1])
        
        return cycle
