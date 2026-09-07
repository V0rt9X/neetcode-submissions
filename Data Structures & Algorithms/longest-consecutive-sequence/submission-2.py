class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)

        for n in numset:
            if n - 1 not in numset:
                length = 0
                while n + length in numset:
                    length += 1
                
                if longest < length:
                    longest = length
        
        return longest