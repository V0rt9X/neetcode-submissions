class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for i,j in zip(s,t):
            s_count[i]+=1
            t_count[j]+=1

        return s_count == t_count