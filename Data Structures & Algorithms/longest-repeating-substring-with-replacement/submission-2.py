class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l=0
        res = 0

        for r, n in enumerate(s):
            counter[n] = counter.get(n, 0) + 1

            k2 = ((r - l) + 1) - max(counter.values())

            if k2 <= k:
                res = max(res, (r-l) + 1)
            else:
                counter[s[l]] -= 1
                l +=1
        
        return res