class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                area = (i - index) * height
                maxArea = max(maxArea, area)
            
            stack.append((index,h))
        
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea