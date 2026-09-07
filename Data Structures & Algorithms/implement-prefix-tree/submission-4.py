class Trie:
    def __init__(self):
        self.chars = {}
        self.EOW = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Trie()
            curr = curr.chars[c]
        
        curr.EOW = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]
        
        return curr.EOW

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]

        return True        
        