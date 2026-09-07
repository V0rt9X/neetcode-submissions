class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        res = []

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        end = 0
        l, r = 0, 0
        while r < len(s):
            end = max(end, lastIndex[s[r]])

            if r == end:
                res.append(r - l + 1)
                l = r + 1
            r += 1
        
        return res


