class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for ind, i  in enumerate(intervals):
            if i[1] < newInterval[0]:
                res.append(i)
            elif i[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[ind: ]
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
        
        res.append(newInterval)
        return res