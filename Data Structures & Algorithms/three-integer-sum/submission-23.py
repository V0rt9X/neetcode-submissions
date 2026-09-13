class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if val > 0:
                return res
            
            if i > 0 and nums[i - 1] == val:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = val + nums[l] + nums[r]

                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res