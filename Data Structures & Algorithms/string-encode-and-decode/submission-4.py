class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(str(len(string)) + '#' + string)
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        l,r = 0,0
        decoded= []

        while l < len(s):
            r = l
            while r < len(s) and s[r]!='#':
                r+=1
            
            length = int(s[l:r])
            decoded.append(s[r+1 : r+length+1])

            l = r + length + 1
        
        return decoded