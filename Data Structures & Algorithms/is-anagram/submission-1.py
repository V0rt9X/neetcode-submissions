class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
                
            Smap, Tmap = {}, {}
                
            for char in range(len(s)):
                Smap[s[char]] = 1 + Smap.get(s[char], 0)
                Tmap[t[char]] = 1 + Tmap.get(t[char], 0)
                    
            return Smap == Tmap
