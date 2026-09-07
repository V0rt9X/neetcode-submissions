class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n + 1)]
        row[n] = 0

        for _ in range(m - 1):
            tmpRow = row.copy()
            for i in range(n - 1, -1, -1):
                tmpRow[i] = tmpRow[i + 1] + row[i]
            
            row = tmpRow
        
        return row[0]

