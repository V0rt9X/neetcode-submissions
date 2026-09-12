class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # key: group key - count chars in str, group - str wich muches to key

        for s in strs:
            counter = [0] * 26 # a: [0], b: [0], ...
            for c in s:
                counter[ord(c) - ord('a')] += 1
            
            groups[tuple(counter)].append(s)

        return list(groups.values())
                