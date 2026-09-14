class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        maxF, res = 0, 0

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            maxF = max(maxF, window[s[r]])

            if (r - l + 1) - maxF <= k:
                res = max(res, r - l + 1)
            else:
                window[s[l]] -= 1
                l += 1
        
        return res