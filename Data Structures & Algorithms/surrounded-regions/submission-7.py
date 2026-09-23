class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def unsur(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            visited.add((r, c))

            for dr, dc in directions:
                unsur(dr + r, dc + c)
        
        for r in range(rows):
            for c in range(cols):
                if r in (0, rows - 1) or c in (0, cols - 1):
                    unsur(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"