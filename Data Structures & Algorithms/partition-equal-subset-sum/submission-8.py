class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        half = sum(nums) // 2

        dp = set([0])

        for n in nums:
            new_dp = dp.copy()
            for val in dp:
                if val + n == half:
                    return True
                
                new_dp.add(val + n)
            
            dp = new_dp
        
        return False