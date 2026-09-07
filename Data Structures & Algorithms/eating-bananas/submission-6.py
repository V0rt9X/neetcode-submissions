class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l,r = 1, max(piles)

        while l<=r:
            mid = (l + r) // 2
            print(mid)

            time = 0
            for pile in piles:
                time += math.ceil(pile / mid) # mid means here also eating speed 
            
            if time <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
            
