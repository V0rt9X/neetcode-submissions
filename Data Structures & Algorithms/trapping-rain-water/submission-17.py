class Solution:
    def trap(self, height: List[int]) -> int:
        leftM, rightM = height[0], height[-1]
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            if leftM < rightM:
                res += leftM - height[l]
                l += 1
                leftM = max(leftM, height[l])
            else:
                res += rightM - height[r]
                r -= 1
                rightM = max(rightM, height[r])
        
        return res