class MedianFinder:

    def __init__(self):
        self.leftH, self.rightH = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftH, -num)

        if self.leftH and self.rightH and self.leftH[0] * -1 > self.rightH[0]:
            heapq.heappush(self.rightH, heapq.heappop(self.leftH) * -1)

        if len(self.leftH) > len(self.rightH) + 1:
            heapq.heappush(self.rightH, heapq.heappop(self.leftH) * -1)
        if len(self.leftH) + 1 < len(self.rightH):
            heapq.heappush(self.leftH, heapq.heappop(self.rightH) * -1)


    def findMedian(self) -> float:
        if len(self.leftH) > len(self.rightH):
            return self.leftH[0] * -1
        elif len(self.leftH) < len(self.rightH):
            return self.rightH[0]
        else:
            return ((self.leftH[0] * -1) + self.rightH[0]) / 2
        