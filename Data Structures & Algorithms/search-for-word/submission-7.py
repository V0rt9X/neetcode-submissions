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
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = Trie()
        root.addWord(word)

        rows, cols = len(board), len(board[0])
        visited = set()
        
        def backtrack(r, c, char):
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                (r, c) in visited or
                board[r][c] not in char.chars):
                return False
            
            visited.add((r, c))
            char = char.chars[board[r][c]]

            if char.EOW:
                return True

            res = (backtrack(r + 1, c, char) or
            backtrack(r - 1, c, char) or
            backtrack(r, c + 1, char) or
            backtrack(r, c - 1, char))

            visited.remove((r, c))

            return res
        


        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, root):
                    return True
        
        return False
        

