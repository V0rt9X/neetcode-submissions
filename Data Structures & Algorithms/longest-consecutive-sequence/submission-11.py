class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in values:
                length = 1
                while n + length in values:
                    length += 1
                res = max(res, length)
        
        return res