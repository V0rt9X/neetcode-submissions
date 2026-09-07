class Trie:
    def __init__(self):
        self.chars = {}
        self.EOW = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Trie()
            curr = curr.chars[c]
        
        curr.EOW = True

    def search(self, word: str) -> bool:

        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                c = word[j] 
            
                if c == ".":
                    for char in curr.chars.values():
                        if dfs(j + 1, char):
                            return True
                
                    return False
                else:
                    if c not in curr.chars:
                        return False
                    curr = curr.chars[c]
            
            return curr.EOW
        
        return dfs(0, self.root)


        
