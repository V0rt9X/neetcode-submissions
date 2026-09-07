class Node:
    def __init__(self):
        self.letters = {}
        self.EOF = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.letters:
                node.letters[c] = Node()
            node = node.letters[c]
        
        node.EOF = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.letters:
                return False
            node = node.letters[c]
        
        return node.EOF

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.letters:
                return False
            node = node.letters[c]
        
        return True
        