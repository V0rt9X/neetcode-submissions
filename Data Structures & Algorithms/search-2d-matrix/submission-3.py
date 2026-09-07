class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0,len(matrix)-1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break
        
        if not top <= bot:
            return False
        
        finded = (top + bot) //2
        l,r = 0, len(matrix[0]) - 1

        while l<=r:
            mid = (l + r) // 2
            
            if matrix[finded][mid] < target:
                l = mid + 1
            elif matrix[finded][mid] > target:
                r = mid - 1
            else:
                return True

        return False