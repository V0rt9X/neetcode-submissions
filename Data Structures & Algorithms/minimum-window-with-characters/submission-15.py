class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        res = ""
        length = float("inf")
        windowS, windowT = defaultdict(int), defaultdict(int)

        for c in t:
            windowT[c] += 1
        
        need = len(windowT)
        have = 0

        l = 0
        for r in range(len(s)):
            windowS[s[r]] += 1

            if windowS[s[r]] == windowT[s[r]]:
                have += 1
            
            while have == need:
                if length >= (r - l + 1):
                    length = (r - l + 1)
                    res = s[l: r + 1]
                
                windowS[s[l]] -= 1
                if windowS[s[l]] < windowT[s[l]]:
                    have -= 1
                
                l += 1
        
        return res
