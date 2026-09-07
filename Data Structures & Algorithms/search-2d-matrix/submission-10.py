class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        lenSubM = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[mid][lenSubM]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        if not l <= r:
            return False

        subM = matrix[(l + r) // 2]
        l,r = 0, lenSubM

        while l <= r:
            mid = (l + r) // 2

            if subM[mid] == target:
                return True
            
            if target < subM[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
