class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxS = 0

        for i, r in enumerate(s):
            while r in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(r)
            maxS = max(maxS, i - l + 1)
        
        return maxS