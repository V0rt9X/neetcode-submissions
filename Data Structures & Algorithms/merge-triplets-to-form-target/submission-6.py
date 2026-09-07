class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i, val in enumerate(t):
                    if target[i] == val:
                        good.add(i)
            
            if len(good) == 3:
                return True
        
        return len(good) == 3