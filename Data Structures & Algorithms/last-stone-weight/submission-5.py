class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]

        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            weight = heapq.heappop(maxHeap) + heapq.heappop(maxHeap) * -1

            if weight:
                heapq.heappush(maxHeap, weight)
        
        heapq.heappush(maxHeap, 0)
        return maxHeap[0] * -1

