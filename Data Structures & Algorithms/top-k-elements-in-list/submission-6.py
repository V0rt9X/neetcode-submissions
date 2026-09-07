class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        bucket = [set() for _ in range(len(nums)+1)]

        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        for n, i in counter.items():
            bucket[i].add(n)
        
        answ = []
        for el in bucket[::-1]:
            for val in el:
                answ.append(val)
                if len(answ) == k:
                    return answ