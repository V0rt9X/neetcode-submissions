class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subSet):
            if i >= len(nums):
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            backtrack(i + 1, subSet)
            subSet.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, subSet)
            
            
        backtrack(0, [])
        return res