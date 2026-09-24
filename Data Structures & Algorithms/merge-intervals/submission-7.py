class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        new_interval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                new_interval = intervals[i]
            else:
                new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        
        res.append(new_interval)
        return res