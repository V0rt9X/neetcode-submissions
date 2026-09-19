class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for am in range(amount + 1):
            for c in coins:
                if am - c >= 0:
                    dp[am] = min(dp[am], 1 + dp[am - c])
        
        return dp[amount] if dp[amount] != float("inf") else -1