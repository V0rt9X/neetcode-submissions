class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answ = defaultdict(list)

        for string in strs:
            counter = [0] * 26

            for char in string:
                index = ord(char) - ord("a")
                counter[index] += 1
            
            answ[tuple(counter)].append(string)
        
        return list(answ.values())