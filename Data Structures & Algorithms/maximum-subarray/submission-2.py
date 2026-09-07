class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subS = 0
        res = nums[0]

        for n in nums:
            if subS < 0:
                subS = 0
            subS += n
            res = max(res, subS)
        
        return res