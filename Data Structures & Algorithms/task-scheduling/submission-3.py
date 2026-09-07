class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timeQ = collections.deque()
        tasks = Counter(tasks)
        maxHeap = [(-task, 0) for task in tasks.values()]
        heapq.heapify(maxHeap)

        cycle = 0
        while maxHeap or timeQ:
            cycle += 1
            if maxHeap:
                task, time = heapq.heappop(maxHeap)

                if task + 1:
                    timeQ.append((task + 1, cycle + n))
            
            if timeQ and timeQ[0][1] == cycle:
                heapq.heappush(maxHeap, timeQ.popleft())
        
        return cycle