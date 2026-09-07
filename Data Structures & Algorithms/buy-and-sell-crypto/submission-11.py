class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        val = prices[l]
        res = 0

        for r in range(len(prices)):
            if prices[r] < val:
                val = prices[r]
                l = r
            
            res = max(res, prices[r] - val)

        return res

            
