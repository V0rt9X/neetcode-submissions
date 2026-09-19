class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones] # o(n)
        heapq.heapify(maxHeap) # o(n)

        while len(maxHeap) > 1:
            summ = heapq.heappop(maxHeap) + heapq.heappop(maxHeap) * -1

            if summ != 0:
                heapq.heappush(maxHeap, summ)
            
        
        return maxHeap[0] * -1 if maxHeap else 0