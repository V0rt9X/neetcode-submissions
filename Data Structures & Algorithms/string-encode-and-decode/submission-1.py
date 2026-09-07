class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        # Loop for encoding each string in strs
        for string in strs:
            enc += str(len(string)) + '#' + string
        
        return enc

    def decode(self, s: str) -> List[str]:
        i=0
        dec = []
        #Loop for through each char in string 's' with i,j index
        while i < len(s):
            j=i
            while s[j] != '#': #Loop for finding # and decode length of string after # by i,j index
                j+=1
            
            length = int(s[i: j]) #Decoding length of string after # by i,j index

            dec.append(s[j+1: j+length+1]) #Appending string in dec(answer list)
            i=j+1+length #Start index shift on end of appended string
        
        return dec
