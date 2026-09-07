class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter1,counter2 = [0] * 26, [0] * 26
        l = 0
        matches = 0

        for r in range(len(s1)):
            counter1[ord(s1[r]) - ord('a')] += 1
            counter2[ord(s2[r]) - ord('a')] += 1

        for i in range(26):
            matches += 1 if counter1[i] == counter2[i] else 0
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            counter2[index] += 1

            if counter2[index] == counter1[index]:
                matches += 1
            elif counter1[index] + 1 == counter2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            counter2[index] -= 1
            if counter2[index] == counter1[index]:
                matches += 1
            elif counter2[index] + 1 == counter1[index]:
                matches -= 1
            
            l+=1
        
        return matches == 26