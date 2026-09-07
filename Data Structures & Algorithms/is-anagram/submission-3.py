class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for sn,tn in zip(s,t):
            counter[sn] = 1 + counter.get(sn, 0)
            counter[tn] = -1 + counter.get(tn, 0)
        
        for n in counter.values():
            if n != 0:
                return False
            
        return True
