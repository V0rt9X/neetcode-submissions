class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in counter:
                counter.remove(s[l])
                l+=1
            counter.add(s[r])
            res = max(res, (r - l) + 1)
        
        return res