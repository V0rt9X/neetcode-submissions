class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        bucket = [set() for _ in range(len(nums)+1)]

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for n, i in counter.items():
            bucket[i].add(n)
        
        answ = []
        for item in bucket[::-1]:
            for n in item:
                answ.append(n)
                if len(answ) == k:
                    return answ