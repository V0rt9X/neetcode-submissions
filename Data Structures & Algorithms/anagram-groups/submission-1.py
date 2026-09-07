class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strHash = {}

        for string in strs:
            letterCount = [0] * 26

            for letter in string:
                letterCount[ord(letter) - ord('a')] += 1
            key = tuple(letterCount)
            
            if key in strHash:
                strHash[key].append(string)
            else:
                strHash[key] = [string]
            
        
        return list(strHash.values())