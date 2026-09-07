class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        res = 0 
        l = 0 
        counter = {}

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            maxF = max(maxF, counter[s[r]])

            diff = ((r - l) + 1) - maxF

            if diff <= k:
                res = max(res, (r - l) + 1)
            else:
                counter[s[l]] -= 1
                l+=1
            
        return res