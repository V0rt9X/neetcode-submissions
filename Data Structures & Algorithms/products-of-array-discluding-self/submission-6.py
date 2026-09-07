class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        pref, postf = 1,1

        for n in nums:
            output.append(pref)
            pref *= n
        
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postf
            postf *= nums[i]
        
        return output