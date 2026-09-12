class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = []
        # 3#abc4#defg

        l, r = 0, 0

        while r < len(s):
            while s[r] != '#':
                r += 1
            
            length = int(s[l: r])
            l = r + 1
            r = r + 1 + length

            decoded.append(s[l: r])
            l = r
        
        return decoded
