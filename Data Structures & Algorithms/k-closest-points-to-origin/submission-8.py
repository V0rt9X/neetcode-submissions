class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # abs(x1 - x2) + abs(y1 - y2)

        minHeap = []
        res = []

        for x, y in points:
            minHeap.append([(x ** 2) + (y ** 2), x, y])
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < k:
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res