class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        path = set()
        def backtrack(i,r,c):
            if i >= len(word):
                return True
            
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i] or
                (r,c) in path):
                return False
            
            path.add((r,c))

            res = (backtrack(i + 1, r + 1, c) or
            backtrack(i + 1, r - 1, c) or
            backtrack(i + 1, r, c + 1) or
            backtrack(i + 1, r, c - 1))

            path.remove((r,c))

            return res
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(0, r, c):
                    return True
        
        return False