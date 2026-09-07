class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_func(nums[1: ]), self.rob_func(nums[: -1]))
        
    
    def rob_func(self, arr):
        rob1, rob2 = 0, 0

        for h in arr:
            total = max(rob1 + h, rob2)
            rob1 = rob2
            rob2 = total
        
        return rob2