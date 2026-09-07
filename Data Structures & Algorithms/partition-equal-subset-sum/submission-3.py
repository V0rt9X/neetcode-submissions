class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        half = sum(nums) // 2
        dp = set()
        dp.add(0)

        for n in nums:
            newDp = dp.copy()
            for subV in dp:
                if subV + n == half:
                    return True
                newDp.add(n + subV)
            
            dp = newDp
        
        return False
