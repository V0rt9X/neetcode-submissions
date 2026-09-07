class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()

        lastEnd = intervals[0][1]

        for start, end in intervals[1: ]:
            if start >= lastEnd:
                lastEnd = end
            else:
                res += 1
                lastEnd = min(end, lastEnd)
        
        return res