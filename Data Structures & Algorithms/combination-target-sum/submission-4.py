class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subC = []
        def backtrack(i, total):
            if total == target:
                res.append(subC.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            subC.append(nums[i])
            backtrack(i, total + nums[i])

            subC.pop()
            backtrack(i + 1, total)
        
        backtrack(0,0)
        return res