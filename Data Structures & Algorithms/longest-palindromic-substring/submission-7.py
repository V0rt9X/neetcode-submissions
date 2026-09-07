class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [-1, -1, 0]
        
        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length >= res[2]:
                    res[0], res[1], res[2] = l, r, length
                
                l -= 1
                r += 1

            l, r = i, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length >= res[2]:
                    res[0], res[1], res[2] = l, r, length
                
                l -= 1
                r += 1
        
        return s[res[0]: res[1] + 1]