class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = defaultdict(int)
        reverse = [[] for _ in range(len(nums)+1)]

        for n in nums:
            bucket[n] += 1
        
        for n, i in bucket.items():
            reverse[i].append(n)
        
        res = []
        for case in reverse[::-1]:
            for n in case:
                res.append(n)
                if len(res) == k:
                    return res