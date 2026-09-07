class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        i = 0
        
        while i < len(gas):
            total += gas[i] - cost[i]
            i += 1

            if total < 0:
                total = 0
                res = i
        
        return res