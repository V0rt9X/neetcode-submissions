class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subSet):
            if i >= len(nums):
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            backtrack(i + 1, subSet)

            subSet.pop()
            backtrack(i + 1, subSet)
        
        backtrack(0, [])
        return res