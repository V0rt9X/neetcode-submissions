class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # [dest, [x, y]]

        for x, y in points:
            dest = x ** 2 + y ** 2
            minHeap.append((dest, [x, y]))
        
        heapq.heapify(minHeap)
        res = []
        while minHeap and k > 0:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        
        return res