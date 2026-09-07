class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(arr):
            if len(arr) == 0:
                return [[]]
            
            perms = dfs(arr[1: ])

            res = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, arr[0])
                    res.append(perm_copy)
            
            return res
        
        return dfs(nums)