class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        end, l = 0, 0
        res = []

        for r in range(len(s)):
            end = max(end, lastIndex[s[r]])

            if r == end:
                res.append((r - l) + 1)
                l = r + 1
        
        return res