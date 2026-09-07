class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, postf = 1,1
        answ = [1] * len(nums)

        for i in range(len(nums)):
            answ[i] = pref
            pref *= nums[i]
        
        for i in range(len(answ)-1,-1,-1):
            answ[i] *= postf
            postf *= nums[i]
        
        return answ