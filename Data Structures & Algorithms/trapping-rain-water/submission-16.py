class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        leftM, rightM = height[l], height[r]
        res = 0

        while l < r:
            if leftM < rightM:
                res += max(0, leftM - height[l])
                l += 1
                leftM = max(leftM, height[l])
            else:
                res += max(0, rightM - height[r])
                r -= 1
                rightM = max(rightM, height[r])
        
        return res