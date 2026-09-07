class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        if l > r:
            return False
        
        row = mid
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            
            if target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            