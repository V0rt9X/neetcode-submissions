class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        sequence = 0

        for n in hashmap:
            if n - 1 not in hashmap:
                length = 1
                while n + length in hashmap:
                    length += 1
                
                sequence = max(sequence, length)
        
        return sequence