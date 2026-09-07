class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l < r:
            while l < r and not self.rule(s[l]):
                l += 1
            while r > l and not self.rule(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True

    
    def rule(self, c1):
        return ((ord('a') <= ord(c1) <= ord('z')) or
               (ord('A') <= ord(c1) <= ord('Z')) or
               (ord('0') <= ord(c1) <= ord('9')))