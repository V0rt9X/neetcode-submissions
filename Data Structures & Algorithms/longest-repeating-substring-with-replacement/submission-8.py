class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l,res,lastMax = 0,0,0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            lastMax = max(lastMax, window[s[r]])

            while (r - l + 1) - lastMax > k:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
