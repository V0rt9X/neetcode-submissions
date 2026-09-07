class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI = {}

        for i, c in enumerate(s):
            lastI[c] = i
        
        end = 0
        l = 0
        res = []

        for r in range(len(s)):
            end = max(end, lastI[s[r]])

            if r == end:
                res.append((r - l) + 1)
                l = r + 1
        
        return res

