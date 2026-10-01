class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        arr = set(nums)
        res = 1

        for val in nums:
            if val - 1 not in arr:
                length = 1
                while val + length in arr:
                    length += 1
                
                res = max(res, length)
        
        return res