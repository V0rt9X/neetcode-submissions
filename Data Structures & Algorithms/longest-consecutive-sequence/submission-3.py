class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numHash = set(nums)

        for n in numHash:
            length = 0
            if n - 1 not in numHash:
                while n + length in numHash:
                    length += 1
            
            longest = max(longest,length)
        
        return longest