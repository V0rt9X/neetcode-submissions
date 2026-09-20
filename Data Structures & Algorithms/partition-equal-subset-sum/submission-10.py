class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set([0])
        half = sum(nums) / 2

        for n in nums:
            new_dp = dp.copy()
            for el in dp:
                if el + n == half:
                    return True
                
                new_dp.add(el + n)
            
            dp = new_dp
        
        return False
