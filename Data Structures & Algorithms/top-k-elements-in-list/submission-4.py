class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # Dict to count each value in nums
        reverse = [[] for _ in range(len(nums)+1)] # List for reversing counted numbers from 'counter' to 'reverse' by index as frequency, key as value

        for n in nums:
            counter[n] = 1 + counter.get(n, 0) #Counting values. get() func to validate if n key exists in dict

        for n, i in counter.items():
            reverse[i].append(n) # Reversing counted values by index as frequency, key as value

        answ = []
        for i in range(len(reverse)-1,0,-1):
            for val in reverse[i]: 
                answ.append(val) # Appending k values in answ list from each list in reversed list
                
                k-=1
                if k == 0:
                    return answ