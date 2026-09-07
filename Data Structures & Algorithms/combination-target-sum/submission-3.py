class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, subComb, total):
            if total == target:
                res.append(subComb.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            subComb.append(nums[i])
            backtrack(i, subComb, total + nums[i])

            subComb.pop()
            backtrack(i + 1, subComb, total)

        backtrack(0, [], 0)
        return res