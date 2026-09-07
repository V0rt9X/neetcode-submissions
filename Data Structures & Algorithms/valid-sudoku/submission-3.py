class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                if val in rows[r] or val in cols[c] or val in box.get((r//3,c//3), set()):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)

                if (r//3, c//3) not in box:
                    box[(r//3,c//3)] = set()
                    box[(r//3,c//3)].add(val)
                else:
                    box[(r//3,c//3)].add(val)
                
        return True
