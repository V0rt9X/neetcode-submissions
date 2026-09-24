class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                dp[j][i] = dp[j][i + 1]
                if j - coins[i] >= 0:
                    dp[j][i] += dp[j - coins[i]][i]
        
        return dp[amount][0]

        # T: O(r * c), S: O(r * c)
        