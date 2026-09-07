class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sC, tC = [0] * 26, [0] * 26

        for i in range(len(s)):
            sC[ord(s[i]) - ord('a')] += 1
            tC[ord(t[i]) - ord('a')] += 1
        
        for c1, c2 in zip(sC, tC):
            if c1 != c2:
                return False
        
        return True