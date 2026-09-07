class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == '.':
                    continue
                
                if n in rows[r] or n in cols[c] or n in box[(r//3, c//3)]:
                    return False
                
                rows[r].add(n)
                cols[c].add(n)
                box[(r//3, c//3)].add(n)
        
        return True