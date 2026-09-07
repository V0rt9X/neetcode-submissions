class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subRM = nums[0]
        subR = 0

        for n in nums:
            if subR < 0:
                subR = 0
            subR += n
            subRM = max(subRM, subR)
        
        return subRM