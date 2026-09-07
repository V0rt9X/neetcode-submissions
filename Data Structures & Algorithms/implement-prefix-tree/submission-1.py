class Node:
    def __init__(self):
        self.chars = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Node()
            curr = curr.chars[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]
        
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]
        
        return True