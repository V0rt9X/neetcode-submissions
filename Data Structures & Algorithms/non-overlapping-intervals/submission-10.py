class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        lastEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEnd:
                lastEnd = min(lastEnd, intervals[i][1])
                res += 1
            else:
                lastEnd = intervals[i][1]
        
        return res