class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-s for s in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > 1:
            first = heapq.heappop(self.maxHeap) * -1
            second = heapq.heappop(self.maxHeap) * -1

            heapq.heappush(self.maxHeap, (first - second) * -1)
        
        return self.maxHeap[0] * -1