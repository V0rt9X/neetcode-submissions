class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l=0
        matches = 0
        counter1,counter2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            counter1[ord(s1[i]) - ord('a')] += 1
            counter2[ord(s2[i]) - ord('a')] += 1
        
        for m in range(26):
            matches += 1 if counter1[m] == counter2[m] else 0
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            counter2[index] += 1
            if counter1[index] == counter2[index]:
                matches += 1
            elif counter1[index] + 1 == counter2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            counter2[index] -= 1
            if counter1[index] == counter2[index]:
                matches += 1
            elif counter2[index] + 1 == counter1[index]:
                matches -= 1
            
            l+=1
        
        return matches == 26
                