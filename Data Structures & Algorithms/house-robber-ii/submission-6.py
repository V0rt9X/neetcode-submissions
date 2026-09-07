class Solution:
    def rob(self, nums: List[int]) -> int:
        def rober(houses):
            rob1, rob2 = 0, 0

            for n in houses:
                tmp = rob2
                rob2 = max(rob1 + n, rob2)
                rob1 = tmp
            
            return rob2
        
        return max(rober(nums[1: ]), rober(nums[: -1]), nums[0])