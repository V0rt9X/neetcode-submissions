class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for l, r in points:
            heapq.heappush(maxHeap, ((l**2 + r**2) * -1, [l, r]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for box in maxHeap:
            res.append(box[1])
        
        return res
