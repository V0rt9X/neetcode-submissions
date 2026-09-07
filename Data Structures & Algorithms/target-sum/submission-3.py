class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for total, way in dp.items():
                new_dp[total + nums[i]] += way
                new_dp[total - nums[i]] += way
            dp = new_dp
        
        return dp[target]

