class MedianFinder:

    def __init__(self):
        self.leftHeap, self.rightHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)

        if self.leftHeap and self.rightHeap and (self.leftHeap[0] * -1) >= self.rightHeap[0]:
            heapq.heappush(self.rightHeap, heapq.heappop(self.leftHeap) * -1)
        
        if len(self.leftHeap) > len(self.rightHeap) + 1:
            heapq.heappush(self.rightHeap, heapq.heappop(self.leftHeap) * -1)
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            heapq.heappush(self.leftHeap, heapq.heappop(self.rightHeap) * -1)

    def findMedian(self) -> float:
        
        if len(self.leftHeap) > len(self.rightHeap):
            return self.leftHeap[0] * -1
        elif len(self.rightHeap) > len(self.leftHeap):
            return self.rightHeap[0]
        else:
            return ((self.leftHeap[0] * -1) + self.rightHeap[0]) / 2
        
        