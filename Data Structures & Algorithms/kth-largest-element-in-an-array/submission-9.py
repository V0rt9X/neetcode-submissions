import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k

        def quickselect(l, r):
            rand_i = random.randint(l, r)
            nums[rand_i], nums[r] = nums[r], nums[rand_i]

            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]

            if p < kth:
                l = p + 1
                return quickselect(l, r)
            elif p > kth:
                r = p - 1
                return quickselect(l, r)
            else:
                return nums[p]
        
        return quickselect(0, len(nums) - 1)