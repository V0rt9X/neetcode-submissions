class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for string in strs:
            encoded.append(str(len(string)) + '#' + string)

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s: return []
        
        decoded = []
        l,r = 0,0

        while r < len(s):
            while r < len(s) and s[r] != '#':
                r += 1
            
            length = int(s[l: r])

            l = r + 1
            r = r + length + 1

            decoded.append(s[l: r])

            l = r
        
        return decoded