class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l, r = 0, 0
        res = []

        for r, n in enumerate(nums):
            while q and nums[q[-1]] <= n:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
        
        return res
