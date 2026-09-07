class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Validation if strings are same length
            return False
        
        counter = [0] * 26 # List of 0 for counting letters by asci value

        for i,j in zip(s,t): # Loop for counting every letter in both lists
            counter[ord(i) - ord('a')] += 1 # From first list we sum every same letter
            counter[ord(j) - ord('a')] -= 1 # From second list we subtract every same letter
        
        for n in counter: # Loop for validating every position in counter list
            if n != 0: # Validation if every position are 0, if not strings not anagrams
                return False
            
        return True 