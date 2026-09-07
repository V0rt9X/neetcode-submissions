class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        lastI = {}

        for i, c in enumerate(s):
            lastI[c] = i

        l, r = 0, 0
        while r < len(s):
            farthest = lastI[s[r]]
            i = l
            while i < farthest:
                farthest = max(farthest, lastI[s[i]])
                i += 1
            
            res.append((farthest - l + 1))
            r = farthest + 1
            l = r
        
        return res