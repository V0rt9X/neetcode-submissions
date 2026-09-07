class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxS = 0

        for r, n in enumerate(s):
            while n in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(n)
            maxS = max(maxS, r - l + 1)
        
        return maxS