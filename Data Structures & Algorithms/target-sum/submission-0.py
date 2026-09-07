class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            new_row = defaultdict(int)
            for curr_sum, count in dp.items():
                new_row[curr_sum + nums[i]] += count
                new_row[curr_sum - nums[i]] += count
            
            dp = new_row
        
        return dp[target]