class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            perSec = (l + r) // 2
            total = 0

            for p in piles:
                total += math.ceil(p / perSec)
            
            if total <= h:
                res = min(res, perSec)
                r = perSec - 1
            else:
                l = perSec + 1
        
        return res