import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k

        def quickselect(l, r):
            r_p = random.randint(l, r)
            nums[r_p], nums[r] = nums[r], nums[r_p]

            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]

            if p < kth:
                return quickselect(p + 1, r)
            elif p > kth:
                return quickselect(l, p - 1)
            else:
                return nums[p]
            
        return quickselect(0, len(nums) - 1)

       