class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref,postf = 1,1
        answ = []

        for n in nums:
            answ.append(pref)
            pref *= n
        
        for i in range(len(nums)-1,-1,-1):
            answ[i] *= postf
            postf *= nums[i]
        
        return answ