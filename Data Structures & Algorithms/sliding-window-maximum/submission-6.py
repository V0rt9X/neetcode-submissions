class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()

        l = 0
        for r, n in enumerate(nums):
            while q and n > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) >= k:
                res.append(nums[q[0]])
                l += 1
        
        return res
