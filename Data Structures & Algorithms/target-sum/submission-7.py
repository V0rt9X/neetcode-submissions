class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for n in nums:
            new_dp = defaultdict(int)
            for amount, ways in dp.items():
                new_dp[amount + n] += ways
                new_dp[amount - n] += ways

            dp = new_dp
        
        return dp[target]

        
