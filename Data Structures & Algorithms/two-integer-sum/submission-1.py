class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}
        
        for i, el in enumerate(nums):
            difference = target - el
            if difference in prevHash:
                return [prevHash[difference], i]
                
            prevHash[el] = i
        
        return
