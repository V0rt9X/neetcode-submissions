class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        counterW,counterT = {},{}
        res, length = [-1,-1], float('inf')
        
        for c in t:
            counterT[c] = counterT.get(c, 0) + 1
        
        need,have = len(counterT), 0
        l=0
        for r in range(len(s)):
            counterW[s[r]] = counterW.get(s[r], 0) + 1

            if s[r] in counterT and counterW[s[r]] == counterT[s[r]]:
                have += 1
            
            while have == need:
                if ((r - l) + 1) < length:
                    res = [l, r]
                    length = (r - l) + 1

                counterW[s[l]] -= 1
                
                if s[l] in counterT and counterW[s[l]] + 1 == counterT[s[l]]:
                    have -= 1
                
                l+=1
        
        l,r = res
        return s[l: r + 1] if length < float("inf") else ""
            

            

