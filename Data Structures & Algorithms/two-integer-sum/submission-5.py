class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Initialization of dictionary for store seen values by value(key), index

        for i, val in enumerate(nums): # Loop for validating and storing values
            diff = target - val # Calculation of difference for finding previos values in seen(dict)

            if diff in seen: # Validation if difference value in seen(dictionary) and returning list of indexses in accordance with condition
                return [seen[diff], i]
            
            seen[val] = i # Creating key by value and assigning it index of this value
        
        return []
