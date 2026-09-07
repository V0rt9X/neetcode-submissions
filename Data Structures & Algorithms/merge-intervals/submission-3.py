class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        output = [intervals[0]]
        lastEnd = intervals[0][1]

        for start, end in intervals[1: ]:
            if start > lastEnd:
                output.append([start, end])
                lastEnd = end
            else:
                lastEnd = max(end, lastEnd)
                output[-1][1] = lastEnd
        
        return output