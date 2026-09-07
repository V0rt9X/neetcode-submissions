class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for string in strs:

            counter = [0] * 26
            for s in string:
                counter[ord(s) - ord('a')] += 1
            key = tuple(counter)

            grouped.setdefault(key, []).append(string)
        
        return list(grouped.values())
