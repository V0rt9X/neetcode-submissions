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
        visited = set()
        res = set()

        def backtrack(r, c, char, subS):
            if (r not in range(rows) or
                c not in range(cols) or
                board[r][c] not in char.chars or
                (r, c) in visited):
                return
            
            visited.add((r, c))
            char = char.chars[board[r][c]]
            subS += board[r][c]

            if char.EOW:
                res.add(subS)
            
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                backtrack(row, col, char, subS)
            
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root, "")
        
        return list(res)