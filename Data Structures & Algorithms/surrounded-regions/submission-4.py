class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def unSurr(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                board[r][c] != 'O'):
                return
            
            visited.add((r, c))
            board[r][c] = 'T'
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

            for dr, dc in directions:
                row, col = dr + r, dc + c
                unSurr(row, col)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in (0, rows - 1) or c in (0, cols - 1)):
                    unSurr(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

