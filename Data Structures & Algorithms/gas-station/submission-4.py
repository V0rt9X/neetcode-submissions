class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            if total < 0:
                total = 0
                start = i
            
            total += (gas[i] - cost[i])
        
        return start
