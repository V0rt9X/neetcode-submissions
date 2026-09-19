class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftMax, leftMin = 1, 1
        res = nums[0]

        for n in nums:
            tmp = leftMax
            leftMax = max(leftMax * n, leftMin * n, n)
            leftMin = min(tmp * n, leftMin * n, n)

            res = max(res, leftMax)
        
        return res