class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        res = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            valid = ((r-l) + 1) - max(counter.values())

            if valid <= k:
                res = max(res, r - l + 1)
            else:
                counter[s[l]] -= 1
                l += 1
            
        return res