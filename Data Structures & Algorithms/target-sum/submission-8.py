class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for n in nums:
            new_dp = defaultdict(int)
            for val, ways in dp.items():
                new_dp[val + n] += ways
                new_dp[val - n] += ways
            dp = new_dp
        
        return dp[target]

