class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l,r = 0, len(s) - 1
        res = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, len(window))
        
        return res