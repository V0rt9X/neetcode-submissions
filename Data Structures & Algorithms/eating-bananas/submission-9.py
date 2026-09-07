class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            perH = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / perH)
            
            if total <= h:
                res = perH
                r = perH - 1
            else:
                l = perH + 1
        
        return res