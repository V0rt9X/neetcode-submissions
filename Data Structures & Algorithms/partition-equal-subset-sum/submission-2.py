class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for n in nums:
            newDp = dp.copy()
            for val in dp:
                if val == target:
                    return True
                
                newDp.add(val + n)
            dp = newDp
        
        return True if target in dp else False