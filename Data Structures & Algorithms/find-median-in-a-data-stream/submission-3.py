class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, num * -1)

        if self.minHeap and self.maxHeap and self.minHeap[0] <= (self.maxHeap[0] * -1):
            heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap) * -1)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap) * -1)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, heapq.heappop(self.minHeap) * -1)
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        else:
            print(self.minHeap[0], self.maxHeap[0])
            return ((self.maxHeap[0] * -1) + self.minHeap[0]) / 2
        