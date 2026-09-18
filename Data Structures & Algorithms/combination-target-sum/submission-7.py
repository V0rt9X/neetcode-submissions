class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path, total):
            if i == len(nums) or total > target:
                return
            
            if total == target:
                res.append(path.copy())
                return 

            path.append(nums[i])
            backtrack(i, path, total + nums[i])

            path.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            
            backtrack(i + 1, path, total)
        
        backtrack(0, [], 0)
        return res
