class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue

            tmp = currMax * n
            currMax = max(tmp, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            
            res = max(res, currMax)
        
        return res