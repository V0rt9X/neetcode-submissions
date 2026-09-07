class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for r, n in enumerate(prices):
            profit = n - prices[l]
            if profit > 0:
                res = max(profit, res)
            else:
                l = r
        
        return res