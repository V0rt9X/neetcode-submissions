class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI = {}
        res = []

        for i, c in enumerate(s):
            lastI[c] = i
        
        l, r = 0, 0
        last = 0

        while r < len(s):
            last = max(last, lastI[s[r]])
            
            if r == last:
                res.append(r - l + 1)
                l = r + 1
            
            r += 1
        
        return res
            
