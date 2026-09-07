class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        maxL,maxR = height[l], height[r]
        res = 0

        while l<r:
            if maxL <= maxR:
                res += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                res += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
        
        return res