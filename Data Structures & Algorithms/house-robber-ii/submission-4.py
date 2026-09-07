class Solution:
    def rob(self, nums: List[int]) -> int:
        def rober(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                tmp = rob2
                rob2 = max(rob2, rob1 + n)
                rob1 = tmp
        
            return rob2
        
        return max(rober(nums[1: ]), rober(nums[: -1]), nums[0])
