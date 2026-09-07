class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        windowS, windowT = defaultdict(int), defaultdict(int)

        res, length = (-1, -1), float("inf")

        for i in range(len(t)):
            windowT[t[i]] += 1
        
        need, have = len(windowT), 0

        l = 0
        for r in range(len(s)):
            windowS[s[r]] += 1
            if s[r] in windowT and windowS[s[r]] == windowT[s[r]]:
                have += 1
            
            
            while have == need:
                if (r - l + 1) < length:
                    res = (l, r)
                    length = r - l + 1
                
                windowS[s[l]] -= 1
                if s[l] in windowT and windowS[s[l]] + 1 == windowT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        
        return s[l: r + 1] if length < float('inf') else ""

