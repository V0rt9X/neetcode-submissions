class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, num * -1)

        if (self.maxHeap and self.minHeap and
            (self.maxHeap[0] * -1) > self.minHeap[0]):
            heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap) * -1)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap) * -1)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, heapq.heappop(self.minHeap) * -1)
        
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        return ((self.maxHeap[0] * -1) + self.minHeap[0]) / 2
        