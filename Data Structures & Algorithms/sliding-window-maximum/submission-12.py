class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []

        l = 0
        for r, val in enumerate(nums):
            while q and nums[q[-1]] <= val:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1
        
        return res