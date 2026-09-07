class Trie:
    def __init__(self):
        self.chars = {}
        self.EOW = False
    
    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Trie()
            curr = curr.chars[c]
        
        curr.EOW = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        visited, res = set(), set()
        
        def backtrack(r, c, char, subS):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or
                board[r][c] not in char.chars):
                return
            
            subS += board[r][c]
            char = char.chars[board[r][c]]
            visited.add((r, c))

            if char.EOW:
                res.add(subS)
            
            backtrack(r + 1, c, char, subS)
            backtrack(r - 1, c, char, subS)
            backtrack(r, c + 1, char, subS)
            backtrack(r, c - 1, char, subS)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root, "")
        
        return list(res)
            
