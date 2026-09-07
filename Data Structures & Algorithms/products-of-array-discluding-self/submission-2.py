class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref,postf = 1,1 # Initialization of prefix and postfix as 1 because firs prefix and postfix always 1. 
        answ = [1] * len(nums) # Initialization answer list

        for i in range(len(nums)): # Loop for prefix logick
            answ[i] = pref # Assigning value by prefix
            pref *= nums[i] # Math logick of prefix and shift +1 for next position
        
        for i in range(len(nums)-1,-1,-1): # Loop for postfix logick
            answ[i] *= postf # Multiplication exist value by postfix
            postf *= nums[i] # Math logick of postfix and shift -1 for next position 

        return answ
