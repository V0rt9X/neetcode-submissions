class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            if heights[l] < heights[r]:
                res = max(res, (r - l) * heights[l])
                l += 1
            else:
                res = max(res, (r - l) * heights[r])
                r -= 1
        
        return res
