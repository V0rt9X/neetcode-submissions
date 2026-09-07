class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        counter = Counter(hand)
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for val in range(first, first + groupSize):
                if counter[val] == 0:
                    return False
                
                counter[val] -= 1

                if counter[val] == 0:
                    if minHeap[0] != val:
                        return False
                    
                    heapq.heappop(minHeap)
        
        return True