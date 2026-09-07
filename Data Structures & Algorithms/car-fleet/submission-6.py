class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        grouped = [(p,s) for p, s in zip(position,speed)]

        for p,s in sorted(grouped, reverse = 1):
            time = (target - p) / s
            stack.append(time)

            if len(stack)>1 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)