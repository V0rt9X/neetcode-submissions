class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for l, r in points:
            minHeap.append(((l**2 + r**2), [l, r]))
        
        heapq.heapify(minHeap)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(minHeap)[1])
        
        return res
            

        