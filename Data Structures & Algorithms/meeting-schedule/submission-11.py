"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i: i.start)

        lastEnd = intervals[0].start

        for i in range(len(intervals)):
            if intervals[i].start < lastEnd:
                return False
            else:
                lastEnd = intervals[i].end
        
        return True
