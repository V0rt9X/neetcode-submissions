class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        counterS1, counterS2 = [0] * 26, [0] * 26

        for c1,c2 in zip(s1,s2):
            counterS1[ord(c1) - ord('a')] += 1
            counterS2[ord(c2) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if counterS1[i] == counterS2[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            i = ord(s2[r]) - ord('a')
            counterS2[i] += 1

            if counterS2[i] == counterS1[i]:
                matches += 1
            elif counterS2[i] - 1 == counterS1[i]:
                matches -= 1
            
            i = ord(s2[l]) - ord('a')
            counterS2[i] -= 1

            if counterS2[i] == counterS1[i]:
                matches += 1
            elif counterS2[i] + 1 == counterS1[i]:
                matches -= 1
            l+=1
        
        return matches == 26

