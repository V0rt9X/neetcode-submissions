class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)

        counter = 0
        for n in nums:
            counter += n
            res = max(res, counter)
            if counter < 0:
                counter = 0
        
        return res