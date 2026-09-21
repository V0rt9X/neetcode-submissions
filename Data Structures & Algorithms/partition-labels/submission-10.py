class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI = {}

        for i, c in enumerate(s):
            lastI[c] = i
        
        l, r = 0, 0
        res = []
        for i in range(len(s)):
            r = max(r, lastI[s[i]])

            if i == r:
                res.append(r - l + 1)
                l = r + 1
            
        return res

        # T: O(n), S: O(n)