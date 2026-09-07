class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subS = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subS.copy())
                return
            
            subS.append(nums[i])
            backtrack(i + 1)

            subS.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res