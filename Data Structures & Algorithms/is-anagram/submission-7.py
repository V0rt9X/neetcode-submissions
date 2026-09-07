class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        counter = {}

        for c1,c2 in zip(s,t):
            counter[c1] = counter.get(c1, 0) + 1
            counter[c2] = counter.get(c2, 0) - 1
        
        for n in counter.values():
            if n != 0:
                return False
        
        return True