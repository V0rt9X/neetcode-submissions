class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for val, i in counter.items():
            buckets[i].append(val)
        
        # [[0], [1], [2], [3], [0], [0], [0]]
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for val in bucket:
                res.append(val)

                if len(res) == k:
                    return res