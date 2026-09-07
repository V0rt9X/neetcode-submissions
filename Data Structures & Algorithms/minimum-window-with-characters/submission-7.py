class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        window, Tmap = {}, {}
        res = [-1,-1], float("inf")

        for c in t:
            Tmap[c] = Tmap.get(c, 0) + 1

        need, have = len(Tmap), 0

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in Tmap and window[s[r]] == Tmap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res[1]:
                    res = [l, r], r-l+1
                window[s[l]] -= 1
                if s[l] in Tmap and window[s[l]] < Tmap[s[l]]:
                    have -= 1
                
                l += 1
        
        l,r = res[0]

        return s[l: r + 1] if res[1] != float("inf") else ""
        
