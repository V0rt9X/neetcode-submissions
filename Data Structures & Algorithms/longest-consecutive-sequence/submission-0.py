class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valset = set(nums) # set of given values
        longest = 0 # counter of longest sequence

        #Cykle for check each unique number in set
        for n in valset:
            if n - 1 not in valset: #Check if actually value less by 1 exsists in set
                lenght = 0
                while n + lenght in valset: #While value bigger then previous in set sequence lenght +1
                    lenght += 1
                
                longest = max(lenght, longest) # Validation of max lenght sequence in set 
        
        return longest #Return result