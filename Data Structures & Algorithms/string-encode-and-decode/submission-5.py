class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(str(len(string)) + '#' + string)
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i,j = 0,0

        while j < len(s):
            while j < len(s) and s[j] != '#':
                j+=1
            
            
            length = int(s[i:j])
            i = j + 1
            j = i + length

            decoded.append(s[i:j])

            i = j
        
        return decoded