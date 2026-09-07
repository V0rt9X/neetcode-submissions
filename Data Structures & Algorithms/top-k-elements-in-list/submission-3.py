class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        reverse = [[] for _ in range((len(nums) + 1))]

        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
        
        for n, i in counter.items():
            reverse[i].append(n)
        
        answ = []

        for i in range(len(reverse)-1,0,-1):
            for n in reverse[i]:
                answ.append(n)
                k-=1
                if k == 0:
                    return answ

