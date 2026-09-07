class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l=0
        r=l+1

        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            
            r+=1
        
        return res