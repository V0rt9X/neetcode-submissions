class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = nums[0]
        counter = 0

        for n in nums:
            counter += n
            maxSub = max(maxSub, counter)

            if counter < 0:
                counter = 0
        
        return maxSub