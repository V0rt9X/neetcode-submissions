class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n - 1] = 1

        for r in range(m - 1, -1, -1):
            new_dp = [0] * (n + 1)
            for c in range(n - 1, -1, -1):
                new_dp[c] = dp[c] + new_dp[c + 1]

            dp = new_dp
        
        return dp[0]

