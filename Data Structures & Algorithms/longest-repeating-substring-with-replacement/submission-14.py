class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowS = defaultdict(int)


        l = 0
        mostF = 0
        res = float("-inf")
        for r in range(len(s)):
            c = s[r]
            windowS[c] += 1

            mostF = max(mostF, windowS[c])

            if (r - l + 1) - mostF <= k:
                res = max(res, (r - l + 1))
            else:
                windowS[s[l]] -= 1
                l += 1
        
        return res