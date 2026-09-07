class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0

        l = 0
        for r, c in enumerate(s):
            while c in window:
                window.remove(s[l])
                l += 1
            
            window.add(c)
            res = max((r - l + 1), res)
        
        return res