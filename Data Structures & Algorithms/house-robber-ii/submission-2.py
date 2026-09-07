class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                total = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = total
            
            return rob2
        
        return max(nums[0], rob(nums[1: ]), rob(nums[: -1]))