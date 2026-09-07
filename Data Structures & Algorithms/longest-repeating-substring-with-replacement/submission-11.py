class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        maxC = res = l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            maxC = max(maxC, counter[s[r]])

            if (r - l + 1) - maxC <= k:
                res = max(res, r - l + 1)
            
            while (r - l + 1) - maxC > k:
                counter[s[l]] -= 1
                l += 1
        return res