class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = max(piles)

        while l <= r:
            perH = (l + r) // 2
            counter = 0
            for p in piles:
                counter += math.ceil(p / perH)
            
            if counter <= h:
                res = min(res, perH)
                r = perH - 1
            else:
                l = perH + 1
        
        return res
