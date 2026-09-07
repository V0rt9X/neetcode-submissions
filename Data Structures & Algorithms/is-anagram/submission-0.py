class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        
        s_map = Counter(s)
        t_map = Counter(t)

        if(s_map == t_map):
            return True
        else:
            return False
