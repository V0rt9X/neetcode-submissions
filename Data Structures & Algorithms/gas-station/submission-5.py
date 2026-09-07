class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0

        pairs = [g - c for g, c in zip(gas, cost)]

        pivot = 0
        for i, t in enumerate(pairs):
            if total < 0:
                total = 0
                pivot = i
            
            total += t
        
        return pivot