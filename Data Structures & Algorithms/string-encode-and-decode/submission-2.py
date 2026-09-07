class Solution:
    def encode(self, strs: List[str]) -> str:
        res = [] # List to store encoded strings to optimize the addition of strings to the end of the returned string

        for string in strs:
            res.append(str(len(string)) + '#' + string) # Converting each string in list by 'x#(x: str)' patern 
        
        return "".join(res) #Join each encoded strings to empty string // here is optimization 

    def decode(self, s: str) -> List[str]:
        i=0
        answ = []
        while i < len(s): # Loop to through each encoded string
            j = i 
            while s[j] != '#': # Loop to find # which give count length of string after #
                j+=1
            
            length = int(s[i:j])
            answ.append(s[j+1 :j + length + 1]) # Appending each string by slice index math
            i = j + length + 1 
        
        return answ