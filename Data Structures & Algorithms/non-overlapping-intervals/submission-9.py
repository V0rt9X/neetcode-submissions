class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()


        lastEnd = intervals[0][1]
        remove = 0
        for start, end in intervals[1: ]:
            if start < lastEnd:
                lastEnd = min(end, lastEnd)
                remove += 1
            else:
                lastEnd = end
        
        return remove