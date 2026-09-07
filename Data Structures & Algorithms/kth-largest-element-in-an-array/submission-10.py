import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k

        l,r = 0, len(nums) - 1

        def quickselect(l, r):
            r_p = random.randint(l, r)
            nums[r], nums[r_p] = nums[r_p], nums[r]

            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]
            
            if p < kth:
                return quickselect(p + 1, r)
            elif p > kth:
                return quickselect(l, p - 1)
            else:
                return nums[p]
            
        return quickselect(l, r)
            

