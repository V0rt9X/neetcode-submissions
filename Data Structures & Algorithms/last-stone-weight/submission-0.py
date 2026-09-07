class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap) * -1
            second = heapq.heappop(maxHeap) * -1

            heapq.heappush(maxHeap, (first - second) * -1)
        
        return maxHeap[0] * -1