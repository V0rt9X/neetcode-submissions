class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subC = 0
        res = nums[0]

        for n in nums:
            if subC < 0:
                subC = 0
            subC += n
            res = max(subC, res)
        
        return res