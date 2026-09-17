class Node:
    def __init__(self):
        self.chars = {}
        self.EOW = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Node()
            
            curr = curr.chars[c]
        
        curr.EOW = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(i, curr):
            if i == len(word):
                return curr.EOW

            for j in range(i, len(word)):
                c = word[j]

                if c == '.':
                    for char in curr.chars.values():
                        if dfs(j + 1, char):
                            return True
                    
                    return False
                else:
                    if c not in curr.chars:
                        return False
                    
                    curr = curr.chars[c]
            
            return curr.EOW

        return dfs(0, curr)