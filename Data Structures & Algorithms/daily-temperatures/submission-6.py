class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                day, temperature = stack.pop()
                res[day] = i - day
            
            stack.append((i, t))
        
        return res