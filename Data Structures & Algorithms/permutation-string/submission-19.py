class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter = [0] * 26
        window = [0] * 26
        matches = 0

        for i in range(len(s1)):
            counter[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        for m in range(26):
            if counter[m] == window[m]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            window[index] += 1
            if window[index] == counter[index]:
                matches += 1
            elif window[index] - 1 == counter[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            window[index] -= 1
            if window[index] == counter[index]:
                matches += 1
            elif window[index] + 1 == counter[index]:
                matches -= 1
            
            l += 1

        
        return matches == 26