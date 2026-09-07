class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        totalMax, totalMin = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0:
                totalMax, totalMin = 1, 1
                continue
            
            tmp = totalMax * n
            totalMax = max(totalMax * n, totalMin * n, n)
            totalMin = min(tmp, totalMin * n, n)

            res = max(res, totalMax)
        
        return res