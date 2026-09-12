class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterS, counterT = [0] * 26, [0] * 26

        for i in range(len(s)):
            counterS[ord(s[i]) - ord("a")] += 1
            counterT[ord(t[i]) - ord("a")] += 1
        
        for val1, val2 in zip(counterS, counterT):
            if val1 != val2:
                return False
        
        return True