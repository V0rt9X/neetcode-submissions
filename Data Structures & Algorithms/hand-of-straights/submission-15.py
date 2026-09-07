class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        cards = Counter(hand)
        minHeap = list(cards)
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for val in range(first, first + groupSize):
                if val not in cards:
                    return False
                
                cards[val] -= 1
                if cards[val] == 0:
                    if minHeap[0] != val:
                        return False
                    heapq.heappop(minHeap)
        
        return True
