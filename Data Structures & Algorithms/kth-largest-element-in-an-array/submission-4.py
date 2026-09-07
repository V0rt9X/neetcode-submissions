import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickselect(l, r):
            r_i = random.randint(l, r)
            nums[r_i], nums[r] = nums[r], nums[r_i]

            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]

            if p > k:
                return quickselect(l, p - 1)
            elif p < k:
                return quickselect(p + 1, r)
            return nums[p]
        
        return quickselect(0, len(nums) - 1)