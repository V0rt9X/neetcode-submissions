class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                res = max(res, (i - index) * height)
            
            stack.append((h, index))

        for h, i in stack:
            res = max(res, (len(heights) - i) * h)
        
        return res
