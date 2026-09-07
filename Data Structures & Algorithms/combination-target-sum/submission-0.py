class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, comb, total):
            if total == target:
                res.append(comb.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            comb.append(nums[i])
            dfs(i, comb, total + nums[i])

            comb.pop()
            dfs(i + 1, comb, total)
        
        dfs(0, [], 0)
        return res