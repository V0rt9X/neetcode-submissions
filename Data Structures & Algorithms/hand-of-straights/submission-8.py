class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        counter = Counter(hand)
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for val in range(first, first + groupSize):
                if val not in counter:
                    return False

                counter[val] -= 1

                if counter[val] == 0:
                    if val != minHeap[0]:
                        return False
                    
                    heapq.heappop(minHeap)
        
        return True
