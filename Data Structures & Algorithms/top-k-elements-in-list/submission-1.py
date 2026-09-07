class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # Dict for counting values in nums.
        buckets = [[] for i in range(len(nums) + 1)] # Creating list of lists for store frequent elements.

        #Loop for counting values in nums.
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        #Loop for reversing items from 'counter' dict and store it by (frequency->index).
        for n, i in counter.items():
            buckets[i].append(n)
        
        #Loop for appending k frequent elements in 'answ' list. First loop for through each (list)element,second for through each element of sublist.
        answ = []
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                answ.append(n)
                k-=1

                if k == 0:
                    return answ
            