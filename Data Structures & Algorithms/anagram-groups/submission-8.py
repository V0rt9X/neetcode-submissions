class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnag = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            
            groupAnag[tuple(counter)].append(s)
        
        return list(groupAnag.values())