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

        for w in words:
            root.addWord(w)
    
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(board), len(board[0])
        visited = set()
        res = set()


        def dfs(r, c, curr, path):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                board[r][c] not in curr.chars):
                return 
            
            path.append(board[r][c])
            visited.add((r, c))
            curr = curr.chars[board[r][c]]
            if curr.EOW:
                res.add("".join(path))

            for dr, dc in directions:
                dfs(dr + r, dc + c, curr, path)
            
            path.pop()
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, [])
        
        return list(res)
