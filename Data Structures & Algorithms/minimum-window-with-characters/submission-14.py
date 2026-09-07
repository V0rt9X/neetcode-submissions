class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        windowS, windowT = defaultdict(int), defaultdict(int)
        res, resL = (-1, -1), float("inf")

        for i in range(len(t)):
            windowT[t[i]] += 1
        
        need, have = len(windowT), 0
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            windowS[c] += 1

            if windowS[c] == windowT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resL:
                    res = (l, r + 1)
                    resL = r - l + 1

                c = s[l]
                windowS[c] -= 1
                if windowS[c] < windowT[c]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r]