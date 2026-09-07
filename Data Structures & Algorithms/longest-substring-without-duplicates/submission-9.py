class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)

        l = 0
        res = 0
        for r in range(len(s)):
            window[s[r]] += 1

            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res