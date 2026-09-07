class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rows[r] or board[r][c] in cols[c] 
                or board[r][c] in box.get((r//3,c//3),set())):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box.setdefault((r//3,c//3), set()).add(board[r][c])

        return True