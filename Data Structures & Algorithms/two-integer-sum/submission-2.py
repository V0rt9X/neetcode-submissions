class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, j in enumerate(nums):
            difference = target - j

            if difference in prevMap:
                return [prevMap[difference], i]

            prevMap[j] = i
        
        return [0,'_',0]