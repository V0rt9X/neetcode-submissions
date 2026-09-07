class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Nmap = defaultdict(int)
        
        for n in nums:
            Nmap[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, i in Nmap.items():
            buckets[i].append(n)
        
        res = []
        for bucket in buckets[len(buckets) - 1: 0: -1]:
            while bucket:
                res.append(bucket.pop())
            
            if len(res) == k:
                return res