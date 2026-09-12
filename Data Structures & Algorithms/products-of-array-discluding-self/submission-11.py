class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, post = 1, 1
        res = []

        for n in nums:
            res.append(pref)
            pref *= n
        
        # 1, 1, 2, 8

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        # 48, 24, 12, 8

        return res