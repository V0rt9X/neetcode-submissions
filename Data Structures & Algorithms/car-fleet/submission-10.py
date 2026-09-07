class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = 1)
        stack = []

        for p, s in pair:
            speed = (target - p) / s
            stack.append(speed)

            if len(stack) > 1 and stack[-1] <= stack [-2]:
                stack.pop()
            
        return len(stack)