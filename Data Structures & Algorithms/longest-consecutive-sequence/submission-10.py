class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 1 if len(nums) else 0

        values = set(nums)

        for n in values:
            if n - 1 not in values:
                length = 1
                while n + length in values:
                    length += 1
                    res = max(res, length)
        
        return res