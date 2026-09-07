class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robber(nums[1: ]), self.robber(nums[: -1]))
    
    def robber(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            total = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = total
        
        return rob2