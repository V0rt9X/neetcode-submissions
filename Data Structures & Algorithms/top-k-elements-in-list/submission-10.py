class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range((len(nums) + 1))]
        counter = Counter(nums)

        for val, fre in counter.items():
            frequency[fre].append(val)
        
        res = []
        for i in range(len(frequency) - 1, -1, -1):
            for val in frequency[i]:
                res.append(val)

                if len(res) == k:
                    return res
