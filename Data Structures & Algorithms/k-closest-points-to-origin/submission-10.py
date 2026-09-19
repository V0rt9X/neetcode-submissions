class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i, cont in enumerate(points): # o(n)
            minHeap.append((cont[0] ** 2 + cont[1] ** 2, i)) #o(n)
        
        heapq.heapify(minHeap) #o(n)

        res = []
        while minHeap and k > 0: #o(n)
            res.append(points[heapq.heappop(minHeap)[1]]) #o(n)
            k -= 1
        
        return res

        # t: o(n + klong), s: o(n)