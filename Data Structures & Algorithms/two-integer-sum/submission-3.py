class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Dict for store and finding answer by difference of values.

        for i, n in enumerate(nums): # Cykle with enumerate function for taking index and value from nums.
            difference = target - n # Difference of target value and element of nums.

            if difference in seen: #Check if the value(key) exsists in dict seen, return index of finded value and index of n value.
                return [seen[difference], i]
            
            seen[n] = i # Seen assignment of n element.