class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, val in enumerate(nums):
            if target - val in diffs:
                return [diffs[target - val], i]
            diffs[val] = i
        
