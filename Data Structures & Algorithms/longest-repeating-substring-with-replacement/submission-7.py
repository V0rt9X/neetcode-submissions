class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l,maxF,res = 0, 0, 0
        
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxF = max(maxF, window[s[r]])

            rep = (r - l + 1) - maxF

            if rep <= k:
                res = max(res, (r - l + 1))
            else:
                window[s[l]] -= 1
                l += 1
        
        return res

