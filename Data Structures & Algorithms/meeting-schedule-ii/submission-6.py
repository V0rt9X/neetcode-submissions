"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        counter = 0
        res = 0
        
        while s < len(start):
            if start[s] < end[e]:
                counter += 1
                res = max(res, counter)
                s += 1
            else:
                e += 1
                counter -= 1
        
        return res