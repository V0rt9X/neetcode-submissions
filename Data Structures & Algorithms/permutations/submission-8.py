class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(arr):
            if len(arr) == 0:
                return [[]]
            
            perms = dfs(arr[1:])

            res = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    p_copy = perm.copy()
                    p_copy.insert(i, arr[0])
                    res.append(p_copy)
            
            return res
        
        return dfs(nums)

