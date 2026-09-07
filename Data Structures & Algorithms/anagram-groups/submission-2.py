class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answ = {} # Dict to store anagrams by key(count of characters).

        for string in strs: # Loop for going through the list of strs.
            count = [0] * 26 # Creating and zeroing counter for characters.
            for char in string: # Loop for going through the string.
                count[ord(char)-ord('a')] += 1 #Counting characters by ASCI.
            
            key = tuple(count) # Creating a tuple key for dictionary asignment.
            if key in answ: # Check if key exsists in answ dict, you can do without this check in code, using defaultdict from collections.
                answ[key].append(string)
            else:
                answ[key] = [string]
        
        return list(answ.values()) 