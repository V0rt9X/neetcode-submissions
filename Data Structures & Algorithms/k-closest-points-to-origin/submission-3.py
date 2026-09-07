class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []

        for x, y in points:
            dest = x ** 2 + y ** 2
            heapq.heappush(minHeap, (dest, [x, y]))
        
        while minHeap and len(res) < k:
            res.append(heapq.heappop(minHeap)[1])
        
        return res