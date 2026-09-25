class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(matrix), len(matrix[0])
        dp = defaultdict(int)

        def dfs(r, c, prev):
            if (r not in range(rows) or
                c not in range(cols) or
                prev >= matrix[r][c]):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + dfs(dr + r, dc + c, matrix[r][c]))
            
            dp[(r, c)] = res
            return res
        
        answ = 1
        for r in range(rows):
            for c in range(cols):
                answ = max(answ, dfs(r, c, -1))
        
        return answ

        # T: O(r * c), S: O(r * c)