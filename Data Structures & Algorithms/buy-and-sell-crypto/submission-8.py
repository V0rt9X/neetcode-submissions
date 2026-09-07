class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0

        for r in range(len(prices)):
            prof = prices[r] - prices[l]
            
            if prices[l] > prices[r]:
                l = r
            else:
                maxProf = max(maxProf, prices[r] - prices[l])
            
            
        return maxProf