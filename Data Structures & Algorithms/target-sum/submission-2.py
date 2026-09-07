class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for curr_sum, ways in dp.items():
                new_dp[curr_sum + nums[i]] += ways
                new_dp[curr_sum - nums[i]] += ways
            
            dp = new_dp
        
        return dp[target]