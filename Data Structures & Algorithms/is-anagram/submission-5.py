class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        counter = [0] * 26

        for let1, let2 in zip(s,t):
            counter[ord(let1)-ord('a')] += 1 
            counter[ord(let2)-ord('a')] -= 1
        
        for n in counter:
            if n != 0:
                return False
        
        return True