class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {} # Dict for storing grouped anagrams

        for string in strs: # Loop through each string in strs
            counter = [0] * 26 # List of 26 zeroes for counting letters in string by ASCII codes
            for el in string: # Loop through each letter in string
                counter[(ord(el)-ord('a'))] += 1 # Counting each letter(el)
            
            key = tuple(counter) # Initializing a key variable to avoid repeatedly calling tuple()
            if key not in grouped: # Validation if key exists in grouped dict
                grouped[key] = [string] # Creating list of str if key not exists in grouped dict
            else:
                grouped[key].append(string) # Appending string to the list of str if key exists in grouped dict
            
        return list(grouped.values()) # Returning list of values from grouped which mean returning list of grouped anagrams
            