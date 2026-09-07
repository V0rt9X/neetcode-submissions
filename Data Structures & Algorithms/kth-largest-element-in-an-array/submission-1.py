import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            rand_ind = random.randint(l, r)
            nums[rand_ind], nums[r] = nums[r], nums[rand_ind]

            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickselect(l, p - 1)
            elif p < k:
                return quickselect(p + 1, r)
            else:
                return nums[p]
        
        return quickselect(0, len(nums) - 1)