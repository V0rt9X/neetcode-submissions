import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # l,r    
        # [1, 2, 3, 4]
        #  0  1  2  3
        # (l + r) // 2 -> (0 + 1) // 2 - > 0
        # res = 2
        
        #1 + 4 + 3 + 2 = 10 <= 9

        # T: O(n * p)
        # T: O(plogn)

        # 3 / 2 = int(1.5) - > 2

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            rate = (l + r) // 2

            counter = 0
            for p in piles:
                counter += math.ceil(p / rate)
            
            if counter <= h:
                r = rate - 1
                res = min(res, rate)
            else:
                l = rate + 1
        
        return res

        # T: O(plogn) S: O(1)

            

