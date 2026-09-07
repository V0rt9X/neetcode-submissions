class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set() # Set for counting unique values
        
        for n in nums: # Loop for validating every n val in set
            if n in uniq: # Validating if n exsists in set
                return True
            
            uniq.add(n) # Appending value in set
        
        return False