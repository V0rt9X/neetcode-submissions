class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        
        seen = set()
        res = False

        for val in range(size):
            if nums[val] in seen:
                res = True
                break
            
            seen.add(nums[val])

        return res