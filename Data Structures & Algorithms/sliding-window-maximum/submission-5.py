class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        l = 0
        res = []

        for r in range(len(nums)):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)

            if l > deq[0]:
                deq.popleft()
            
            if (r + 1) >= k:
                res.append(nums[deq[0]])
                l+=1
        
        return res