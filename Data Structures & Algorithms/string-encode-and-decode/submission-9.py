class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        l, r = 0, 0
        
        decoded = []

        while r < len(s):
            while s[r] != '#':
                r += 1
            
            length = int(s[l: r])

            decoded.append(s[r + 1: r + length + 1])
            
            r = r + length + 1
            l = r
        
        return decoded