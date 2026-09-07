class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            res = heapq.heappop(maxHeap) + heapq.heappop(maxHeap) * -1
            if res != 0:
                heapq.heappush(maxHeap, res)
        
        return maxHeap[0] * -1 if maxHeap else 0

