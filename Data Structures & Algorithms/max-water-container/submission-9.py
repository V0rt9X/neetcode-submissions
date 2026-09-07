class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxLeft, maxRight = heights[l], heights[r]
        most = 0
        
        while l < r:
            if maxLeft < maxRight:
                most = max(most, (r - l) * heights[l])
                l += 1
                maxLeft = heights[l]
            else:
                most = max(most, (r - l) * heights[r])
                r -= 1
                maxRight = heights[r]
        
        return most