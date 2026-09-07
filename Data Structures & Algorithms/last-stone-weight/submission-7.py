class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH = [-s for s in stones]
        heapq.heapify(maxH)

        while len(maxH) > 1:
            s1, s2 = -heapq.heappop(maxH), heapq.heappop(maxH)

            afterSmash = s1 + s2
            if afterSmash:
                heapq.heappush(maxH, -afterSmash)
        
        return -maxH[0] if maxH else 0
