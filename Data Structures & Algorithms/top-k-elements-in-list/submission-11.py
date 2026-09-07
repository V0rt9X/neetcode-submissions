class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        frequency = [[] for _ in range(len(nums) + 1)]

        for val, freq in counter.items():
            frequency[freq].append(val)
        
        res = []
        for i in range(len(frequency) - 1, -1, -1):
            for val in frequency[i]:
                res.append(val)

                if len(res) == k:
                    return res

