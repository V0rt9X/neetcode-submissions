class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for val, i in counter.items():
            freq[i].append(val)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
            
        
        return res