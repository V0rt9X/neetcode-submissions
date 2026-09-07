class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_now, rob_on_next = 0, 0

        for n in nums:
            total = max(rob_on_next, rob_now + n)
            rob_now = rob_on_next
            rob_on_next = total
        
        return rob_on_next