class MedianFinder:

    def __init__(self):
        self.lHeap, self.rHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lHeap, -num) 

        if self.lHeap and self.rHeap and (self.lHeap[0] * -1) >= self.rHeap[0]:
            heapq.heappush(self.rHeap, heapq.heappop(self.lHeap) * -1)
        
        if len(self.lHeap) + 1 < len(self.rHeap):
            heapq.heappush(self.lHeap, heapq.heappop(self.rHeap) * -1)
        if len(self.lHeap) > len(self.rHeap) + 1:
            heapq.heappush(self.rHeap, heapq.heappop(self.lHeap) * -1)
        

    def findMedian(self) -> float:
        if len(self.lHeap) < len(self.rHeap):
            return self.rHeap[0]
        elif len(self.lHeap) > len(self.rHeap):
            return self.lHeap[0] * -1
        else:
            return (self.lHeap[0] * -1 + self.rHeap[0]) / 2
    
    # T: O(n log n), S: O(n)