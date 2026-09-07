class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        remove = 0

        lastEnd = intervals[0][1]
        for start, end in intervals[1: ]:
            if lastEnd > start:
                lastEnd = min(end, lastEnd)
                remove += 1
            else:
                lastEnd = end
        
        return remove