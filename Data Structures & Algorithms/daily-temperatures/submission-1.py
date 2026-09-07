class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                stackI = stack[-1][1]
                result[stackI] = i - stackI
                stack.pop()
            stack.append((n,i))
        
        return result