class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArr = 0
        maxArr = float("-inf")

        for n in nums:
            subArr += n
            maxArr = max(maxArr, subArr)
            if subArr < 0:
                subArr = 0
        
        return maxArr