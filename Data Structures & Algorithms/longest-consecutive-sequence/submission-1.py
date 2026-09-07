class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 # Counter of longest consecutive sequence
        numset = set(nums) # Set to validate values by O(1)

        for val in numset:
            if val - 1 not in numset: # Validation if value - 1 exsists in numset if not loop starts counting length of sequence
                length = 0
                while val + length in numset: 
                    length+=1
                
                if longest < length: # Validation if counted length of sequence bigger then previous longest sequence
                    longest = length
            
        return longest
