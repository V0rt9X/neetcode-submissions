class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        intervals.sort()

        minHeap = []

        i = 0
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1
        
        output = []
        for q in queries:
            output.append(res[q])
        
        return output


