class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)] # List of sets for store every value in row
        col = [set() for _ in range(9)] # List of sets for store every value in column
        box = defaultdict(set) # Dictionary for store values in sub-boxes by tuple keys

        for r in range(9): # Loop for iterating every row in board
            for c in range(9): # Loop for iterating every column in board
                val = board[r][c]
                if val == '.': # Validate if position is empty.
                    continue
                
                if val in row[r] or val in col[c] or val in box[(r//3),(c//3)]: # Validate if value in row,col or sub-box.
                    return False
                
                row[r].add(val) # Adding value in row set
                col[c].add(val) # Adding value in col set (column)
                box[(r//3,c//3)].add(val) # Adding value in sub-box
        
        return True