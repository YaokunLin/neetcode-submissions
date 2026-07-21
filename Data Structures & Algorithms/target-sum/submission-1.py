from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            new_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                new_dp[cur_sum + num] += count
                new_dp[cur_sum - num] += count
            dp = new_dp
        return dp[target]

        