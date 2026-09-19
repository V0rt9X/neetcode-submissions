class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i, cont in enumerate(points):
            minHeap.append((cont[0] ** 2 + cont[1] ** 2, i))
        
        heapq.heapify(minHeap)

        res = []
        while minHeap and k > 0:
            res.append(points[heapq.heappop(minHeap)[1]])
            k -= 1
        
        return res