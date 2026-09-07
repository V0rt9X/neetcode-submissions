import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k
        
        def quickselect(l, r):
            rand_p = random.randint(l, r)
            nums[r], nums[rand_p] = nums[rand_p], nums[r]

            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]

            if p < kth:
                return quickselect(p + 1, r)
            elif p > kth:
                return quickselect(l, p - 1)
            else:
                return nums[p]
        
        return quickselect(0, len(nums) - 1)
