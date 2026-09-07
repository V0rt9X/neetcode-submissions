class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(i, r, c):
            if i == len(word):
                return True
            
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                board[r][c] != word[i]):
                return False
            
            visited.add((r, c))
            res = (backtrack(i + 1, r + 1, c) or
                   backtrack(i + 1, r - 1, c) or
                   backtrack(i + 1, r, c + 1) or
                   backtrack(i + 1, r, c - 1))
            
            visited.remove((r, c))
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == word[0]):
                    if backtrack(0, r, c):
                        return True
        
        return False
