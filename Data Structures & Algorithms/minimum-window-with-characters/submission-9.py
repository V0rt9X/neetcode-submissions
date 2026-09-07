class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        res, length = (-1,-1), float("inf")
        windowS = defaultdict(int)
        windowT = defaultdict(int)

        for c in t:
            windowT[c] += 1

        have, need = 0, len(windowT)
        
        l = 0
        for r in range(0, len(s)):
            val = s[r]
            windowS[val] += 1


            if val in windowT and windowS[val] == windowT[val]:
                have += 1
            
            while have == need:
                if (r - l + 1) <= length:
                    res, length = (l, r + 1), r - l + 1

                val = s[l]
                windowS[val] -= 1

                if val in windowT and windowS[val] + 1 == windowT[val]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l: r] if length < float("inf") else ""
            
            
        