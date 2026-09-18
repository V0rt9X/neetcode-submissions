class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        perms = self.permute(nums[1:])

        res = []
        for perm in perms:
            for i in range(len(perm) + 1):
                p_copy = perm.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res