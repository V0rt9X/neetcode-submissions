class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[0], heights[-1]
        res = 0

        while l < r:
            if maxL <= maxR:
                res = max(res, (r - l) * heights[l])
                l += 1
                maxL = heights[l]
            else:
                res = max(res, (r - l) * heights[r])
                r -= 1
                maxR = heights[r]
            
        return res