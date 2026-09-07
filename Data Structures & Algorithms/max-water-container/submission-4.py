class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        maxL,maxR = heights[l], heights[r]

        while l < r:
            if maxL <= maxR:
                maxArea = max(maxArea, (r - l) * heights[l])
                l += 1
                maxL = heights[l]
            else:
                maxArea = max(maxArea, (r - l) * heights[r])
                r -= 1
                maxR = heights[r]
            
        return maxArea
