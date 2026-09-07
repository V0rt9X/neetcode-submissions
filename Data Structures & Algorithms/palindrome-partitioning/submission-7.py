class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        def backtrack(i, subS):
            if i >= len(s):
                res.append(subS.copy())
                return
            
            for j in range(i, len(s)):
                if isPali(i, j):
                    subS.append(s[i: j + 1])
                    backtrack(j + 1, subS)
                    subS.pop()
        
        backtrack(0, [])
        return res

                