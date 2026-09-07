class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subS):
            if i >= len(nums):
                res.append(subS[::])
                return
            
            subS.append(nums[i])
            backtrack(i + 1, subS)

            subS.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, subS)
        
        backtrack(0,[])
        return res