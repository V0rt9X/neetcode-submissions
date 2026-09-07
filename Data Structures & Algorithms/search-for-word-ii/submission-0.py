class Tnode:
    def __init__(self):
        self.chars = {}
        self.EOW = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = Tnode()
            curr = curr.chars[c]
        
        curr.EOW = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Tnode()

        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def backtrack(r, c, char, path):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or 
                board[r][c] not in char.chars):
                return
            
            visited.add((r, c))
            char = char.chars[board[r][c]]
            path += board[r][c]

            if char.EOW:
                res.add(path)
            
            backtrack(r + 1, c, char, path)
            backtrack(r - 1, c, char, path)
            backtrack(r, c + 1, char, path)
            backtrack(r, c - 1, char, path)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root, "")
        
        return list(res)