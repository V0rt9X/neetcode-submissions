class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0
        intervals.sort()

        lastEnd = intervals[0][1]

        for start, end in intervals[1: ]:
            if lastEnd > start:
                lastEnd = min(lastEnd, end)
                remove += 1
            else:
                lastEnd = end
        
        return remove