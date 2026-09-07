class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPali(i, j, s):
                    part.append(s[i: j+1])
                    backtrack(j + 1)
                    part.pop()
            
        
        def isPali(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                
                i += 1
                j -= 1
            
            return True
        
        backtrack(0)
        return res
