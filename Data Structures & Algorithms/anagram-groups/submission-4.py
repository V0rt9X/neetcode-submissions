class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {} # Dict to store grouped anagrams

        for string in strs:
            counter = [0] * 26 # Counter to calculate letters and make key by this
            for c in string: 
                counter[ord(c) - ord('a')] += 1
            
            grouped.setdefault(tuple(counter), []).append(string) # Logick of appending string in grouped dict
        
        return list(grouped.values())