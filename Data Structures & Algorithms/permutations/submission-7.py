class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def backtrack(nums):
            if not len(nums):
                return [[]]
            
            perms = backtrack(nums[1:])

            res = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, nums[0])
                    res.append(p_copy)
            
            return res
        
        return backtrack(nums)