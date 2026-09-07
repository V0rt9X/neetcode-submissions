class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        if not top <= bot:
            return False
        
        box = (top + bot) // 2
        l,r = 0, len(matrix[box])-1
        while l <= r:
            mid = (l+r) // 2
            
            if matrix[box][mid] < target:
                l = mid + 1
            elif matrix[box][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False