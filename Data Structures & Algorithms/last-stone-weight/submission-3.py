class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            weight = (heapq.heappop(maxHeap) * -1) - (heapq.heappop(maxHeap) * -1)
            
            heapq.heappush(maxHeap, weight * -1)
        

        return maxHeap[0] * -1