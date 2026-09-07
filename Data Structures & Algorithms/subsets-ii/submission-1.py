class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(i, comb):
            if i >= len(nums):
                res.append(comb.copy())
                return
            
            comb.append(nums[i])
            backtrack(i + 1, comb)

            comb.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, comb)
        
        backtrack(0, [])
        return res