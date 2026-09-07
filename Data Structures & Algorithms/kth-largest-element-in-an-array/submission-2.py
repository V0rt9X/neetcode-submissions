import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def dfs(l, r):
            r_i = random.randint(l, r)
            nums[r_i], nums[r] = nums[r], nums[r_i]

            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                
            nums[r], nums[p] = nums[p], nums[r]

            if p > k:
                return dfs(l, p - 1)
            elif p < k:
                return dfs(p + 1, r)
            else:
                return nums[p]
        
        return dfs(0, len(nums) - 1)