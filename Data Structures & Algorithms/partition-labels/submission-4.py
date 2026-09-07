class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI = {}

        for i, c in enumerate(s):
            lastI[c] = i

        l, r = 0, 0
        res = []

        while r < len(s):
            i = l
            while i <= r:
                r = max(r, lastI[s[i]])
                i += 1
            
            res.append((r - l + 1))
            r = r + 1
            l = r
        
        return res
