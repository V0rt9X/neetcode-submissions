class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, postf = 1,1
        res = []

        for n in nums:
            res.append(pref)
            pref *= n
        
        for i in range(len(res)-1,-1,-1):
            res[i] *= postf
            postf *= nums[i]
        
        return res