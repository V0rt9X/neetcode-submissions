class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int) # -> total: ways
        dp[0] = 1

        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for total, ways in dp.items():
                new_dp[total + nums[i]] += ways
                new_dp[total - nums[i]] += ways
            dp = new_dp
        
        return dp[target]

