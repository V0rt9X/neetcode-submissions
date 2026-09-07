class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot = 0,len(matrix) - 1

        while top<=bot:
            mid = (top + bot) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if not top <= bot:
            return False
        
        mid = (top + bot) // 2
        l,r = 0, len(matrix[0]) - 1
        

        while l<=r:
            m = (l + r) // 2

            if matrix[mid][m] == target:
                return True

            if matrix[mid][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False