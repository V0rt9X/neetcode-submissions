class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0

        counter = 0
        for i in range(len(gas)):
            if counter < 0:
                start = i
                counter = 0
            counter += gas[i] - cost[i]
        
        return start

        # T: O(n), S: O(1)